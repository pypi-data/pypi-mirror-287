from mlflow.store.tracking.abstract_store import AbstractStore
import requests
from mlflow.entities import Experiment, Metric, Run, RunInfo
import logging
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_aiworkspace20210204 import models as aiwork_space_20210204_models
import os
import pai_mlflow.utils.model_utils as pai_mlflow_plugin_utils
from mlflow.exceptions import MissingConfigException, MlflowException
from pai_mlflow.utils import ai_workspace_utils

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class PluginPAIRestStore(AbstractStore):
    """
    Plugin PAI Rest Store
    """
    def __init__(self, store_uri=None, artifact_uri=None):
        self.is_plugin = True
        self.workspace_id = os.getenv("WORKSPACE_ID")
        access_key_id = os.getenv("ACCESS_KEY_ID")
        access_key_secret = os.getenv("ACCESS_KEY_SECRET")
        region = os.getenv("REGION")
        self.ai_workspace_client = ai_workspace_utils.create_ai_workspace_client(access_key_id, access_key_secret, region)
        self.artifact_uri = artifact_uri
        self.store = store_uri
        super().__init__()

    def _call_endpoint(self, api, json_body, endpoint=None):
        endpoint = "{target_url}/api/2.0/mlflow/{api}"
        response = requests.post(endpoint, json=json_body)
        logger.debug(f"Calling endpoint: {endpoint}")
        logger.debug(f"JSON body: {json_body}")
        return response.json()

    def list_experiments(self, view_type=None):
        return self._call_endpoint("experiments/list", {"view_type": view_type})

    def create_experiment(self, name, artifact_location=None, tags=None):
        artifact_location = 'oss://pai-quickstart-test-beta-beijing.oss-cn-beijing-internal.aliyuncs.com/wzy/output/44_2_2_3_1/'
        label: list[aiwork_space_20210204_models.LabelInfo] = []
        for item in tags:
            label.append(aiwork_space_20210204_models.LabelInfo(key=item[0], value=item[1]))
        create_experiment_request = aiwork_space_20210204_models.CreateExperimentRequest(
            name=name, artifact_uri=artifact_location, workspace_id=self.workspace_id,
            labels=label, accessibility="PRIVATE")
        response = self.ai_workspace_client.create_experiment(create_experiment_request)
        return response.body.experiment_id

    def get_experiment(self, experiment_id):
        experiment_response = self.ai_workspace_client.get_experiment(experiment_id)
        if experiment_response:
            return pai_mlflow_plugin_utils.trans_pai_experiment_response_to_mlflow_experiment(experiment_response)
        else:
            raise MlflowException(
                f"Experiment '{experiment_id}' does not exist."
            )

    def get_experiment_by_name(self, name):
        """
        获取实验
        """
        # todo 提供独立接口，鉴于实验名称唯一
        logger.info(self.artifact_uri)
        logger.info(self.store)
        list_experiment_request = aiwork_space_20210204_models.ListExperimentRequest(name=name, workspace_id=self.workspace_id)
        experiment_list = self.ai_workspace_client.list_experiment(list_experiment_request).body.experiments
        if experiment_list and len(experiment_list) > 0 and experiment_list[0].name == name:
            experiment = experiment_list[0]
            logger.info('find experiment: %s' % experiment)
            return pai_mlflow_plugin_utils.trans_pai_experiment_to_mlflow_experiment(experiment)
        else:
            logger.info('not find experiment: %s' % name)
            return None

    def delete_experiment(self, experiment_id):
        return self._call_endpoint("experiments/delete", {"experiment_id": experiment_id})

    def restore_experiment(self, experiment_id):
        return self._call_endpoint("experiments/restore", {"experiment_id": experiment_id})

    def rename_experiment(self, experiment_id, new_name):
        return self._call_endpoint("experiments/update", {"experiment_id": experiment_id, "new_name": new_name})

    def create_run(self, experiment_id, user_id, start_time, tags, run_name):
        return self._call_endpoint("runs/create", {
            "experiment_id": experiment_id,
            "user_id": user_id,
            "start_time": start_time,
            "tags": tags
        })

    def get_run(self, run_id):
        return self._call_endpoint("runs/get", {"run_id": run_id})

    def update_run_info(self, run_id, run_status, end_time,run_name):
        return self._call_endpoint("runs/update", {
            "run_id": run_id,
            "status": run_status,
            "end_time": end_time
        })

    def delete_run(self, run_id):
        return self._call_endpoint("runs/delete", {"run_id": run_id})

    def restore_run(self, run_id):
        return self._call_endpoint("runs/restore", {"run_id": run_id})

    def log_metric(self, run_id, metric):
        return self._call_endpoint("metrics/log", {"run_id": run_id, "metrics": [metric]})

    def log_param(self, run_id, param):
        return self._call_endpoint("params/log", {"run_id": run_id, "params": [param]})

    def set_tag(self, run_id, tag):
        return self._call_endpoint("tags/log", {"run_id": run_id, "tags": [tag]})

    # 添加其他需要的方法...