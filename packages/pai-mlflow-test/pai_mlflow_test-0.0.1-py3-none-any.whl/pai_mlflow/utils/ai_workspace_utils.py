from alibabacloud_aiworkspace20210204.client import Client as AIWorkSpace20210204Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_aiworkspace20210204 import models as aiwork_space_20210204_models


def create_ai_workspace_client(access_key_id: str, access_key_secret: str,
                               region: str) -> AIWorkSpace20210204Client:
    config = open_api_models.Config(
        access_key_id=access_key_id, access_key_secret=access_key_secret
    )
    config.endpoint = f"aiworkspace.{region}.aliyuncs.com"
    return AIWorkSpace20210204Client(config)
