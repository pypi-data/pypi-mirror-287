# -*- coding=utf-8
import logging
import time
from functools import wraps

import requests
from requests import ConnectionError, Timeout

from spider_cloud_cos.scos_auth import CosS3Auth
from spider_cloud_cos.scos_comm import *
from spider_cloud_cos.scos_config import CosConfig
from spider_cloud_cos.scos_exception import CosServiceError, CosClientError, CosException
from spider_cloud_cos.version import __version__

logger = logging.getLogger(__name__)


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} returned: {result}")
        return result

    return wrapper


def retry(retries):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            exception_logbuf = []
            for j in range(retries + 1):
                try:
                    if j != 0:
                        time.sleep(j)
                    return func(*args, **kwargs)
                except (ConnectionError, Timeout) as e:
                    exception_logbuf.append(f'Retry {j}: {str(e)}')
                    if j == retries:
                        logger.exception(exception_logbuf)
                        raise CosClientError(exception_logbuf)
                except Exception as e:
                    exception_logbuf.append(f'Error on attempt {j}: {str(e)}')
                    logger.exception(exception_logbuf)
            raise CosServiceError(exception_logbuf)

        return wrapper

    return decorator


class RequestSender:
    def __init__(self, conf, session, retry=3, use_built_in_pool=True):
        self._conf = conf
        self._session = session
        self._retry = retry
        self._use_built_in_pool = use_built_in_pool

    def handle_built_in_connection_pool_by_pid(self):
        if not CosS3Client._built_in_sessions:
            return

        if not self._use_built_in_pool:
            return

        if CosS3Client._built_in_pid == os.getpid():
            return

        with threading.Lock():
            if CosS3Client._built_in_pid == os.getpid():
                return

            CosS3Client._built_in_sessions.close()
            CosS3Client._built_in_sessions = self.generate_built_in_connection_pool(self._conf._pool_connections,
                                                                                    self._conf._pool_maxsize)
            CosS3Client._built_in_pid = os.getpid()
            self._session = CosS3Client._built_in_sessions
            logger.info("Bound built-in connection pool when new processor. maxsize=%d,%d",
                        self._conf._pool_connections, self._conf._pool_maxsize)

    @retry(3)
    @log_decorator
    def send_request(self, method, url, bucket=None, timeout=30, **kwargs):
        if self._conf._timeout is not None:
            timeout = self._conf._timeout
        if self._conf._ua is not None:
            kwargs['headers']['User-Agent'] = self._conf._ua
        else:
            kwargs['headers']['User-Agent'] = 'cos-python-sdk-v' + __version__
        if self._conf._token is not None:
            kwargs['headers']['x-cos-security-token'] = self._conf._token

        if self._conf._ip is not None:
            if self._conf._domain is not None:
                kwargs['headers']['Host'] = self._conf._domain
            elif bucket is not None:
                kwargs['headers']['Host'] = self._conf.get_host(Bucket=bucket)

        if not self._conf._keep_alive:
            kwargs['headers']['Connection'] = 'close'

        self.handle_built_in_connection_pool_by_pid()

        method_func = getattr(self._session, method.lower())
        for _ in range(self._retry + 1):
            try:
                return method_func(url, timeout=timeout, proxies=self._conf._proxies, **kwargs)
            except (ConnectionError, Timeout):
                continue
        raise CosClientError(f"Failed to {method} {url} after {self._retry} retries")


class CosS3Client:
    _built_in_sessions = None
    _built_in_pid = 0

    def __init__(self, conf, retry=1, session=None):
        self._conf = conf
        self._retry = retry
        self._session = session or self._get_built_in_session()
        self._use_built_in_pool = session is None

    def _get_built_in_session(self):
        if not CosS3Client._built_in_sessions:
            with threading.Lock():
                if not CosS3Client._built_in_sessions:
                    CosS3Client._built_in_sessions = self._generate_built_in_connection_pool()
                    CosS3Client._built_in_pid = os.getpid()
        return CosS3Client._built_in_sessions

    @log_decorator
    def _generate_built_in_connection_pool(self):
        session = requests.session()
        adapter = requests.adapters.HTTPAdapter(pool_connections=self._conf._pool_connections,
                                                pool_maxsize=self._conf._pool_maxsize)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        logger.info("Generated built-in connection pool. maxsize=%d,%d", self._conf._pool_connections,
                    self._conf._pool_maxsize)
        return session

    def get_conf(self):
        return self._conf

    @log_decorator
    def put_object(self, Bucket, Body, Key, EnableMD5=False, **kwargs):
        headers = kwargs.get('headers', {})
        url = self._conf.uri(bucket=Bucket, path=Key)
        if EnableMD5:
            md5_str = get_content_md5(Body)
            if md5_str:
                headers['Content-MD5'] = md5_str
        sender = RequestSender(self._conf, self._session, self._retry, self._use_built_in_pool)
        return sender.send_request(
            method='PUT',
            url=url,
            bucket=Bucket,
            auth=CosS3Auth(self._conf, Key),
            data=Body,
            headers=headers)


class ConfigManager:
    @staticmethod
    @retry(3)
    def get_conf():
        confs = requests.get(
            'http://mediaproxy.zhuaninc.com/innerApi/getTmpFederationToken?pathSign=2a16Kte43GK')
        if confs.status_code != 200:
            raise CosServiceError(message="获取pathSign失败：【mediaproxy.zhuaninc.com】", status_code=confs.status_code)

        conf_json = confs.json()
        if int(conf_json["respCode"]) != 0:
            raise CosException("获取pathSign接口失败")
        return conf_json["respData"]


class CosClientWrapper:
    def __init__(self):
        self.config = None
        self.client = None
        self.conf = None

    def put_object(self, body, name):
        self.conf = ConfigManager.get_conf()
        self.config = CosConfig(**self.conf)
        self.client = CosS3Client(self.config)
        file_name = f'{self.conf["pathPrefix"][1:]}{name}'
        bucket = self.conf['bucket']
        get_files = self.client.put_object(bucket, body, file_name)
        result = {"url": to_cdn(get_files.url, self.config._origin_domain, bucket, self.config._region)}
        result.update(get_files.headers)
        return result
