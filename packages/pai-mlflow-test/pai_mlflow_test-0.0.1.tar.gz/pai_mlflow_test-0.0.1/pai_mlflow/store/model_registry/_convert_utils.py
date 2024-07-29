from mlflow.entities.model_registry import ModelVersion as ModelVersionObj
from mlflow.entities.model_registry import ModelVersionTag as ModelVersionTagObj
from mlflow.entities.model_registry import RegisteredModel as RegisteredModelObj
from mlflow.entities.model_registry import RegisteredModelTag as RegisteredModelTagObj

from pai_mlflow.vendor.alibabacloud_mlflow20210312.models import *


def registered_model_to_mlflow_obj(registered_model: RegisteredModel):
    return RegisteredModelObj(
        registered_model.name,
        int(registered_model.creation_timestamp),
        int(registered_model.last_updated_timestamp)
        if registered_model.last_updated_timestamp is not None
        else None,
        registered_model.description,
        [model_version_to_mlflow_obj(m) for m in registered_model.latest_versions],
        registered_model.tags,
    )


def model_version_to_mlflow_obj(model_version: ModelVersion):
    return ModelVersionObj(
        model_version.name,
        model_version.version,
        int(model_version.creation_timestamp),
        int(model_version.last_updated_timestamp)
        if model_version.last_updated_timestamp is not None
        else None,
        model_version.description,
        model_version.user_id,
        model_version.current_stage,
        model_version.source,
        model_version.run_id,
        model_version.status,
        model_version.status_message,
        [model_version_tag_to_mlflow_obj(i) for i in model_version.tags]
        if model_version.tags
        else None,
        model_version.run_link,
    )


def model_version_tag_to_mlflow_obj(model_version_tag: ModelVersionTag):
    return ModelVersionTagObj(model_version_tag.key, model_version_tag.value)


def registered_model_tag_to_mlflow_obj(registered_model_tag: RegisteredModelTag):
    return RegisteredModelTagObj(registered_model_tag.key, registered_model_tag.value)
