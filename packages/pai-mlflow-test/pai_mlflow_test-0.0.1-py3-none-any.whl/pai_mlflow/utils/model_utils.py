from mlflow.entities import Experiment, Metric, Run, RunInfo, LifecycleStage
from alibabacloud_aiworkspace20210204 import models as ai_workspace_20210204_models


def trans_pai_experiment_to_mlflow_experiment(pai_experiment: ai_workspace_20210204_models.Experiment):
    """
    Transfer PAI experiment to MLflow experiment
    """
    experiment = Experiment(experiment_id= pai_experiment.experiment_id, name=pai_experiment.name,
                            artifact_location=pai_experiment.artifact_uri, lifecycle_stage=LifecycleStage.ACTIVE)
    return experiment


def trans_mlflow_experiment_to_pai_experiment(mlflow_experiment: Experiment):
    """
    Transfer MLflow experiment to PAI experiment
    """
    pai_experiment = ai_workspace_20210204_models.Experiment(
        experiment_id=mlflow_experiment.experiment_id,
        name=mlflow_experiment.name,artifact_uri=mlflow_experiment.artifact_location)
    return pai_experiment


def trans_pai_experiment_response_to_mlflow_experiment(pai_experiment_response: ai_workspace_20210204_models.GetExperimentResponse):
    """
    Transfer PAI experiment response body to MLflow experiment
    """
    tag = {}
    for item in pai_experiment_response.body.labels:
        tag[item.key] = item.value
    experiment = Experiment(experiment_id= pai_experiment_response.body.experiment_id,
                            name=pai_experiment_response.body.name,
                            artifact_location=pai_experiment_response.body.artifact_uri,
                            lifecycle_stage=LifecycleStage.ACTIVE,
                            creation_time=pai_experiment_response.body.gmt_create_time,
                            last_update_time=pai_experiment_response.body.gmt_modified_time,
                            tags=tag)
    return experiment