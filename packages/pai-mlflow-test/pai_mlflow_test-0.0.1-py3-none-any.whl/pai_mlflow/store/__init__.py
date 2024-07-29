from functools import wraps
from urllib import parse

from Tea.exceptions import UnretryableException

from pai_mlflow.exceptions import PaiMlflowException


def _get_alibabacloud_client(store_uri):
    from alibabacloud_tea_openapi.models import Config
    from pai_mlflow.vendor.alibabacloud_mlflow20210312.client import Client

    uri = parse.urlparse(store_uri)
    from pai_mlflow.utils.__global import (
        PAI_ACCESS_KEY_ID,
        PAI_ACCESS_KEY_SECRET,
    )

    config = Config(
        access_key_id=PAI_ACCESS_KEY_ID,
        access_key_secret=PAI_ACCESS_KEY_SECRET,
        endpoint=uri.netloc,
    )
    return Client(config)


def get_pai_tracking_store(store_uri, **_):
    from pai_mlflow.store.tracking import PaiTrackingStore

    return PaiTrackingStore(_get_alibabacloud_client(store_uri))


def get_pai_model_registry_store(store_uri, **_):
    from pai_mlflow.store.model_registry import PaiModelRegistryStore

    return PaiModelRegistryStore(_get_alibabacloud_client(store_uri))


def get_oss_artifact_repository(artifact_uri):
    from pai_mlflow.store.artifact import OssArtifactRepository

    return OssArtifactRepository(artifact_uri)


def get_paiflow_run_context():
    from pai_mlflow.store.tracking.context.paiflow_context import (
        PaiflowRunContext,
    )

    return PaiflowRunContext()


def catch_api_exceptions(method=None, should_raise=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except UnretryableException as e:
                if (
                    "error_code" in e.data
                    and e.data["error_code"] == "RESOURCE_DOES_NOT_EXIST"
                ):
                    if should_raise:
                        raise PaiMlflowException(e.data)
                    return None
                else:
                    if PaiMlflowException.is_valid(e.data):
                        raise PaiMlflowException(e.data)
                    else:
                        raise e

        return wrapper

    return decorator(method) if method else decorator
