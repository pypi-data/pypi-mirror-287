from mlflow.entities import Experiment as ExperimentObj
from mlflow.entities import Metric as MetricObj
from mlflow.entities import Run as RunObj
from mlflow.entities import RunData as RunDataObj
from mlflow.entities import RunInfo as RunInfoObj

from pai_mlflow.vendor.alibabacloud_mlflow20210312.models import *


def experiment_to_mlflow_obj(experiment: Experiment):
    return ExperimentObj(
        experiment.experiment_id,
        experiment.name,
        experiment.artifact_location,
        experiment.lifecycle_stage,
        experiment.tags,
    )


def run_to_mlflow_obj(run: Run):
    return RunObj(run_info_to_mlflow_obj(run.info), run_data_to_mlflow_obj(run.data))


def run_info_to_mlflow_obj(run_info: RunInfo):
    return RunInfoObj(
        run_info.run_uuid,
        run_info.experiment_id,
        run_info.user_id,
        run_info.status,
        int(run_info.start_time) if run_info.start_time else None,
        int(run_info.end_time) if run_info.end_time else None,
        run_info.lifecycle_stage,
        run_info.artifact_uri,
        run_info.run_id,
    )


def run_data_to_mlflow_obj(run_data: RunData):
    return RunDataObj(
        [metric_to_mlflow_obj(m) for m in (run_data.metrics or [])],
        run_data.params,
        run_data.tags,
    )


def metric_to_mlflow_obj(metric: Metric):
    return MetricObj(
        metric.key,
        metric.value,
        int(metric.timestamp) if metric.timestamp else None,
        int(metric.step) if metric.step else None,
    )
