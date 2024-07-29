import os

from mlflow.tracking.context.abstract_context import RunContextProvider

from pai_mlflow.consts import (
    PAI_MLFLOW_PARENT_RUN_ID,
    PAI_RUN_ID,
    PAI_MLFLOW_RUN_NAME,
    PAI_NODE_ID,
    PAI_USER_ID,
    PAI_STUDIO_EXPERIMENT_ID,
    PAI_PIPELINE_METADATA_IDENTIFIER,
    SOURCE_PAI_STUDIO,
    PAI_PAIFLOW_PIPELINES,
    PAI_AI_WORKSPACE_ID,
)

from mlflow.utils.mlflow_tags import (
    MLFLOW_PARENT_RUN_ID as MLFLOW_PARENT_RUN_ID_TAG,
    MLFLOW_RUN_NAME as MLFLOW_RUN_NAME_TAG,
    MLFLOW_USER as MLFLOW_USER_TAG,
    MLFLOW_SOURCE_TYPE as MLFLOW_SOURCE_TYPE_TAG,
    MLFLOW_SOURCE_NAME as MLFLOW_SOURCE_NAME_TAG,
)
from pai_mlflow.utils.mlflow_tags import (
    PAI_STUDIO_EXPERIMENT_TAG,
    PAIFLOW_RUN_TAG,
    PAIFLOW_NODE_TAG,
    PAI_WORKSPACE_TAG,
)


class PaiflowRunContext(RunContextProvider):
    def in_context(self):
        return (
            PAI_PAIFLOW_PIPELINES in os.environ
            and os.environ[PAI_PAIFLOW_PIPELINES] == "true"
        )

    ENV_TAG_MAPPING = {
        PAI_MLFLOW_PARENT_RUN_ID: MLFLOW_PARENT_RUN_ID_TAG,
        PAI_MLFLOW_RUN_NAME: MLFLOW_RUN_NAME_TAG,
        PAI_USER_ID: MLFLOW_USER_TAG,
        PAI_PIPELINE_METADATA_IDENTIFIER: MLFLOW_SOURCE_NAME_TAG,
        PAI_AI_WORKSPACE_ID: PAI_WORKSPACE_TAG,
        PAI_STUDIO_EXPERIMENT_ID: PAI_STUDIO_EXPERIMENT_TAG,
        PAI_RUN_ID: PAIFLOW_RUN_TAG,
        PAI_NODE_ID: PAIFLOW_NODE_TAG,
    }

    def get_tags_by_env(self):
        """
        Get tags from environment variables.

        Returns:
            dict: tags key-value from environment.

        """
        return {
            tag_name: os.environ[env_var]
            for env_var, tag_name in self.ENV_TAG_MAPPING.items()
            if env_var in os.environ
        }

    def tags(self):
        tags = self.get_tags_by_env()
        tags[MLFLOW_SOURCE_TYPE_TAG] = SOURCE_PAI_STUDIO
        return tags
