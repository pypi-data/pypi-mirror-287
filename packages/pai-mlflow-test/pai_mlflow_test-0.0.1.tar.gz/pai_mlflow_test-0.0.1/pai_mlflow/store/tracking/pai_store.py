import os

from mlflow.entities import ViewType
from mlflow.store.tracking.abstract_store import AbstractStore
from pai_mlflow.consts import (
    PAI_MLFLOW_LOG_METRIC_TO_PARENT_RUN,
    PAI_MLFLOW_PARENT_RUN_ID,
)

from pai_mlflow.store import catch_api_exceptions
from pai_mlflow.store.tracking._convert_utils import *
from pai_mlflow.vendor.alibabacloud_mlflow20210312.client import Client


class PaiTrackingStore(AbstractStore):
    def __init__(self, client: Client):
        super().__init__()
        self.client = client

    @catch_api_exceptions
    def list_experiments(self, view_type=ViewType.ACTIVE_ONLY):
        body = self.client.list_experiments(ListExperimentsRequest(str(view_type))).body
        return [experiment_to_mlflow_obj(b) for b in body.experiments]

    @catch_api_exceptions
    def create_experiment(self, name, artifact_location):
        body = self.client.create_experiment(
            CreateExperimentRequest(name, artifact_location)
        ).body
        return body.experiment_id

    @catch_api_exceptions(should_raise=True)
    def get_experiment(self, experiment_id):
        body = self.client.get_experiment(GetExperimentRequest(experiment_id)).body
        return experiment_to_mlflow_obj(body.experiment)

    @catch_api_exceptions
    def get_experiment_by_name(self, experiment_name):
        resp = self.client.get_experiment_by_name(
            GetExperimentByNameRequest(experiment_name)
        )
        return experiment_to_mlflow_obj(resp.body.experiment)

    @catch_api_exceptions
    def delete_experiment(self, experiment_id):
        self.client.delete_experiment(DeleteExperimentRequest(experiment_id))
        return experiment_id

    @catch_api_exceptions
    def restore_experiment(self, experiment_id):
        self.client.restore_experiment(RestoreExperimentRequest(experiment_id))
        return experiment_id

    @catch_api_exceptions
    def rename_experiment(self, experiment_id, new_name):
        self.client.update_experiment(UpdateExperimentRequest(new_name, experiment_id))
        return experiment_id

    @catch_api_exceptions
    def get_run(self, run_id):
        body = self.client.get_run(GetRunRequest(run_id)).body
        return run_to_mlflow_obj(body.run)

    @catch_api_exceptions
    def update_run_info(self, run_id, run_status, end_time):
        from mlflow.entities import RunStatus

        body = self.client.update_run(
            UpdateRunRequest(run_id, RunStatus.to_string(run_status), end_time)
        ).body
        return run_info_to_mlflow_obj(body.run_info)

    @catch_api_exceptions
    def create_run(self, experiment_id, user_id, start_time, tags):
        run_tags = [RunTag(tag.key, tag.value) for tag in tags] if tags else []
        body = self.client.create_run(
            CreateRunRequest(experiment_id, user_id, start_time, run_tags)
        ).body
        return run_to_mlflow_obj(body.run)

    @catch_api_exceptions
    def delete_run(self, run_id):
        self.client.delete_run(DeleteRunRequest(run_id))
        return run_id

    @catch_api_exceptions
    def restore_run(self, run_id):
        self.client.restore_run(RestoreRunRequest(run_id))
        return run_id

    @catch_api_exceptions
    def get_metric_history(self, run_id, metric_key):
        body = self.client.get_metric_history(
            GetMetricHistoryRequest(run_id, metric_key)
        ).body
        return [metric_to_mlflow_obj(i) for i in body.metrics]

    @catch_api_exceptions
    def _search_runs(
        self,
        experiment_ids,
        filter_string,
        run_view_type,
        max_results,
        order_by,
        page_token,
    ):
        experiment_ids = [str(experiment_id) for experiment_id in experiment_ids]
        body = self.client.search_runs(
            SearchRunsRequest(
                experiment_ids,
                filter_string,
                run_view_type,
                max_results,
                list(order_by) if order_by else None,
                page_token,
            )
        ).body
        return [run_to_mlflow_obj(run) for run in body.runs], body.next_page_token

    @catch_api_exceptions
    def log_batch(self, run_id, metrics, params, tags):
        metrics = [Metric(m.key, m.value, m.timestamp, m.step) for m in metrics]
        params = [Param(p.key, p.value) for p in params]
        tags = [RunTag(t.key, t.value) for t in tags]
        self.client.log_batch(LogBatchRequest(run_id, metrics, params, tags))
        self._log_metric_on_parent_run(metrics)

    @catch_api_exceptions
    def record_logged_model(self, run_id, mlflow_model):
        self.client.log_model(LogModelRequest(run_id, mlflow_model.to_json()))

    @catch_api_exceptions(should_raise=True)
    def set_experiment_tag(self, experiment_id, tag):
        self.client.set_experiment_tag(
            SetExperimentTagRequest(experiment_id, tag.key, tag.value)
        )

    @staticmethod
    def is_log_metric_to_parent():
        return os.environ.get(PAI_MLFLOW_LOG_METRIC_TO_PARENT_RUN, "false") == "true"

    @staticmethod
    def get_parent_run_id():
        return os.environ.get(PAI_MLFLOW_PARENT_RUN_ID)

    # PaiTrackingStore log metrics to parent_run if environment variable PAI_MLFLOW_LOG_METRIC_TO_PARENT_ENABLE=true.
    def _log_metric_on_parent_run(self, metrics):
        if not type(self).is_log_metric_to_parent():
            return

        parent_run_id = type(self).get_parent_run_id()
        if not parent_run_id:
            return
        self.client.log_batch(
            LogBatchRequest(parent_run_id, metrics=metrics, params=[], tags=[])
        )
