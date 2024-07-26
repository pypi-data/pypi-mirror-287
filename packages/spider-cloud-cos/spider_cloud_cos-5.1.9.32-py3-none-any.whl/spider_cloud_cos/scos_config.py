# -*- coding=utf-8

import logging
import sys

from spider_cloud_cos.scos_comm import *
from spider_cloud_cos.scos_exception import CosClientError

# python 3.10报错"module 'collections' has no attribute 'Iterable'"，这里先规避
if sys.version_info.major >= 3 and sys.version_info.minor >= 10:
    import collections.abc

    collections.Iterable = collections.abc.Iterable

logger = logging.getLogger(__name__)


class CosConfig(object):
    """config类，保存用户相关信息"""

    def __init__(self, *args, **kwargs):
        """初始化，保存用户的信息
        :param _appid(string): 用户APPID.
        :param _region(string): 地域信息.
        :param tmpSecretId(string): 秘钥SecretId.
        :param tmpSecretKey(string): 秘钥SecretKey.
        :param _token(string): 临时秘钥使用的token.
        :param scheme(string): http/https
        :param _timeout(int): http超时时间.
        :param Access_id(string): 秘钥AccessId(兼容).
        :param Access_key(string): 秘钥AccessKey(兼容).
        :param Secret_id(string): 秘钥SecretId(兼容).
        :param Secret_key(string): 秘钥SecretKey(兼容).
        :param _endpoint(string): endpoint.
        :param _ip(string): 访问COS的ip
        :param _port(int):  访问COS的port
        :param _anonymous(bool):  是否使用匿名访问COS
        :param _ua(string):  使用自定义的UA来访问COS
        :param _proxies(dict):  使用代理来访问COS
        :param _domain(string):  使用自定义的域名来访问COS
        :param _service_domain(string):  使用自定义的域名来访问cos service
        :param _keep_alive(bool):       是否使用长连接
        :param _pool_connections(int):  连接池个数
        :param _pool_maxsize(int):      连接池中最大连接数
        :param _allow_redirects(bool):  是否重定向
        :param _sign_host(bool):  是否将host算入签名
        :param _endpoint_ci(string):  ci的endpoint
        :param _enable_old_domain(bool):  是否使用旧的myqcloud.com域名访问COS
        :param _enable_internal_domain(bool):  是否使用内网域名访问COS
        :param _sign_params(bool): 是否将请求参数算入签名
        """
        self._appid = to_unicode(kwargs.get('appid', None))
        self._token = to_unicode(kwargs.get('token', None))
        self._timeout = kwargs.get('timeout', None)
        self._region = kwargs.get('region', None)
        self._endpoint = kwargs.get('endpoint', None)
        self._endpoint_ci = kwargs.get('endpoint_ci', None)
        self._endpoint_pic = kwargs.get('endpoint_pic', None)
        self._ip = to_unicode(kwargs.get('ip', None))
        self._port = kwargs.get('port', None)
        self._anonymous = kwargs.get('anonymous', None)
        self._ua = kwargs.get('ua', None)
        self._proxies = kwargs.get('proxies', None)
        self._domain = kwargs.get('domain', None)
        self._service_domain = kwargs.get('service_domain', None)
        self._keep_alive = kwargs.get('keep_alive', True)
        self._pool_connections = kwargs.get('pool_connections', 10)
        self._pool_maxsize = kwargs.get('pool_maxsize', 10)
        self._allow_redirects = kwargs.get('allow_redirects', False)
        self._sign_host = kwargs.get('sign_host', True)
        self._copy_part_threshold_size = SINGLE_UPLOAD_LENGTH
        self._enable_old_domain = kwargs.get('enable_old_domain', True)
        self._enable_internal_domain = kwargs.get('enable_internal_domain', True)
        self._sign_params = kwargs.get('sign_params', True)
        self._auto_switch_domain_on_retry = kwargs.get('auto_switch_domain_on_retry', False)
        self._origin_domain = kwargs.get('originDomain', None)
        self.path = 'kfyq_spider/plat_315/'

        if self._domain is None:
            self._endpoint = format_endpoint(self._endpoint, self._region, u'cos.', self._enable_old_domain,
                                             self._enable_internal_domain)
        if kwargs.get('scheme', None) is None:
            Scheme = u'https'
        Scheme = to_unicode(Scheme)
        if (Scheme != u'http' and Scheme != u'https'):
            raise CosClientError('Scheme can be only set to http/https')
        self._scheme = Scheme

        # 格式化ci的endpoint 不支持自定义域名的
        # ci暂不支持新域名
        self._endpoint_ci = format_endpoint(self._endpoint_ci, self._region, u'ci.', True, False)
        self._endpoint_pic = format_endpoint(self._endpoint_ci, self._region, u'pic.', True, False)

        # 兼容(SecretId,SecretKey)以及(AccessId,AccessKey)
        SecretId = kwargs.get('tmpSecretId', None)
        SecretKey = kwargs.get('tmpSecretKey', None)
        Secret_id = kwargs.get('Secret_id', None)
        Secret_key = kwargs.get('Secret_key', None)
        Access_id = kwargs.get('Access_id', None)
        Access_key = kwargs.get('Access_key', None)
        CredentialInstance = kwargs.get('CredentialInstance', None)

        if (SecretId and SecretKey):
            self._secret_id = self.convert_secret_value(SecretId)
            self._secret_key = self.convert_secret_value(SecretKey)
        elif (Secret_id and Secret_key):
            self._secret_id = self.convert_secret_value(Secret_id)
            self._secret_key = self.convert_secret_value(Secret_key)
        elif (Access_id and Access_key):
            self._secret_id = self.convert_secret_value(Access_id)
            self._secret_key = self.convert_secret_value(Access_key)
        elif (CredentialInstance and hasattr(CredentialInstance, "secret_id") and hasattr(CredentialInstance,
                                                                                          "secret_key") and hasattr(
                CredentialInstance, "token")):
            self._secret_id = None
            self._secret_key = None
            self._credential_inst = CredentialInstance
        elif self._anonymous:
            self._secret_id = None
            self._secret_key = None
            self._credential_inst = None
        else:
            raise CosClientError('SecretId and SecretKey is Required!')

    def uri(self, bucket=None, path=None, endpoint=None, domain=None, useAppid=False):
        """拼接url

        :param bucket(string): 存储桶名称.
        :param path(string): 请求COS的路径.
        :return(string): 请求COS的URL地址.
        """
        scheme = self._scheme
        # 拼接请求的url,默认使用bucket和endpoint拼接请求域名
        # 使用自定义域名时则使用自定义域名访问
        # 指定ip和port时,则使用ip:port方式访问,优先级最高
        if domain is None:
            domain = self._domain
        if domain is not None:
            url = domain
        else:
            if endpoint is None:
                endpoint = self._endpoint

            if bucket is not None:
                bucket = format_bucket(bucket, self._appid)
                url = u"{bucket}.{endpoint}".format(bucket=bucket, endpoint=endpoint)
            else:
                if useAppid:
                    url = u"{appid}.{endpoint}".format(appid=self._appid, endpoint=endpoint)
                else:
                    url = u"{endpoint}".format(endpoint=endpoint)
        if self._ip is not None:
            url = self._ip
            if self._port is not None:
                url = u"{ip}:{port}".format(ip=self._ip, port=self._port)

        if path is not None:
            if not path:
                raise CosClientError("Key is required not empty")
            path = to_unicode(path)
            if path[0] == u'/':
                path = path[1:]
            path = quote(to_bytes(path), '/-_.~')
            path = path.replace('./', '.%2F')

            request_url = u"{scheme}://{url}/{path}".format(
                scheme=to_unicode(scheme),
                url=to_unicode(url),
                path=to_unicode(path)
            )
        else:
            request_url = u"{scheme}://{url}/".format(
                scheme=to_unicode(scheme),
                url=to_unicode(url)
            )
        return request_url

    def get_host(self, Bucket=None, Appid=None):
        """传入bucket名称,根据endpoint获取Host名称
        :param Bucket(string): bucket名称
        :return (string): Host名称
        """
        if Bucket is not None:
            return u"{bucket}.{endpoint}".format(bucket=format_bucket(Bucket, self._appid), endpoint=self._endpoint)
        if Appid is not None:
            return u"{appid}.{endpoint}".format(appid=Appid, endpoint=self._endpoint)

    def set_ip_port(self, IP, Port=None):
        """设置直接访问的ip:port,可以不指定Port,http默认为80,https默认为443
        :param IP(string): 访问COS的ip
        :param Port(int):  访问COS的port
        :return None
        """
        self._ip = to_unicode(IP)
        self._port = Port

    def set_credential(self, SecretId, SecretKey, Token=None):
        """设置访问的身份,包括secret_id,secret_key,临时秘钥token默认为空
        :param SecretId(string): 秘钥SecretId.
        :param SecretKey(string): 秘钥SecretKey.
        :param Token(string): 临时秘钥使用的token.
        """
        self._secret_id = self.convert_secret_value(SecretId)
        self._secret_key = self.convert_secret_value(SecretKey)
        self._token = self.convert_secret_value(Token)

    def set_copy_part_threshold_size(self, size):
        if size > 0:
            self._copy_part_threshold_size = size

    def convert_secret_value(self, value):
        value = to_unicode(value)

        if value.endswith(' ') or value.startswith(' '):
            raise CosClientError('secret_id and secret_key cannot contain spaces at the beginning and end')

        return value
