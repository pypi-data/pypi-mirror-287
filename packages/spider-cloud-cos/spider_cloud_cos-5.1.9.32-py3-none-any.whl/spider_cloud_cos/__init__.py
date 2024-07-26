from __future__ import absolute_import
import pkgutil

from spider_cloud_cos.scos_auth import CosS3Auth
from spider_cloud_cos.scos_client import (CosS3Client)
from spider_cloud_cos.scos_config import CosConfig
from spider_cloud_cos.scos_exception import CosClientError, CosServiceError, CosException
from spider_cloud_cos.version import __version__

VERSION = __version__

__all__ = [
    CosS3Auth,
    CosS3Client,
    CosConfig,
    CosClientError,
    CosServiceError,
    CosException,
    VERSION
]