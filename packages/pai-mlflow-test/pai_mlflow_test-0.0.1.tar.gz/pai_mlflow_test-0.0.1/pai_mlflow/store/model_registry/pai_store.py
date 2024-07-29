from mlflow.store.entities.paged_list import PagedList
from mlflow.store.model_registry.abstract_store import AbstractStore

from pai_mlflow.vendor.alibabacloud_mlflow20210312.client import Client
from pai_mlflow.store.model_registry._convert_utils import *
from pai_mlflow.store import catch_api_exceptions


class PaiModelRegistryStore(AbstractStore):
    def __init__(self, client: Client):
        super().__init__()
        self.client = client

    @catch_api_exceptions
    def create_registered_model(self, name, tags=None, description=None):
        registered_model_tag = (
            [RegisteredModelTag(tag.key, tag.value) for tag in tags] if tags else []
        )
        body = self.client.create_registered_model(
            CreateRegisteredModelRequest(name, registered_model_tag, description)
        ).body
        return registered_model_to_mlflow_obj(body.registered_model)

    @catch_api_exceptions
    def update_registered_model(self, name, description):
        body = self.client.update_registered_model(
            UpdateRegisteredModelRequest(name, description)
        ).body
        return registered_model_to_mlflow_obj(body.registered_model)

    @catch_api_exceptions
    def rename_registered_model(self, name, new_name):
        body = self.client.rename_registered_model(
            RenameRegisteredModelRequest(name, new_name)
        ).body
        return registered_model_to_mlflow_obj(body.registered_model)

    @catch_api_exceptions
    def delete_registered_model(self, name):
        self.client.delete_registered_model(DeleteRegisteredModelRequest(name))

    @catch_api_exceptions
    def list_registered_models(self, max_results, page_token):
        body = self.client.list_registered_models(
            ListRegisteredModelsRequest(max_results, page_token)
        ).body
        return PagedList(
            [registered_model_to_mlflow_obj(i) for i in body.registered_models]
            if body.registered_models
            else [],
            body.next_page_token,
        )

    @catch_api_exceptions
    def search_registered_models(
        self, filter_string=None, max_results=None, order_by=None, page_token=None
    ):
        body = self.client.search_registered_models(
            SearchRegisteredModelsRequest(
                filter_string, max_results, list(order_by), page_token
            )
        ).body
        return PagedList(
            [registered_model_to_mlflow_obj(i) for i in body.registered_models]
            if body.registered_models
            else [],
            body.next_page_token,
        )

    @catch_api_exceptions
    def get_registered_model(self, name):
        body = self.client.get_registered_model(GetRegisteredModelRequest(name)).body
        return registered_model_to_mlflow_obj(body.registered_model)

    @catch_api_exceptions
    def get_latest_versions(self, name, stages=None):
        body = self.client.get_latest_versions(
            GetLatestVersionsRequest(name, stages)
        ).body
        return [model_version_to_mlflow_obj(i) for i in body.model_versions]

    @catch_api_exceptions
    def set_registered_model_tag(self, name, tag):
        self.client.set_registered_model_tag(
            SetRegisteredModelTagRequest(name, tag.key, tag.value)
        )

    @catch_api_exceptions
    def delete_registered_model_tag(self, name, key):
        self.client.delete_registered_model_tag(
            DeleteRegisteredModelTagRequest(name, key)
        )

    @catch_api_exceptions
    def create_model_version(
        self, name, source, run_id=None, tags=None, run_link=None, description=None
    ):
        body = self.client.create_model_version(
            CreateModelVersionRequest(
                name,
                source,
                run_id,
                [ModelVersionTag(i.key, i.value) for i in tags] if tags else None,
                run_link,
                description,
            )
        ).body
        return model_version_to_mlflow_obj(body.model_version)

    @catch_api_exceptions
    def update_model_version(self, name, version, description):
        body = self.client.update_model_version(
            UpdateModelVersionRequest(name, version, description)
        ).body
        return model_version_to_mlflow_obj(body.model_version)

    @catch_api_exceptions
    def transition_model_version_stage(
        self, name, version, stage, archive_existing_versions
    ):
        body = self.client.transition_model_version_stage(
            TransitionModelVersionStageRequest(
                name, version, stage, archive_existing_versions
            )
        ).body
        return model_version_to_mlflow_obj(body.model_version)

    @catch_api_exceptions
    def delete_model_version(self, name, version):
        self.client.delete_model_version(DeleteModelVersionRequest(name, version))

    @catch_api_exceptions
    def get_model_version(self, name, version):
        body = self.client.get_model_version(GetModelVersionRequest(name, version)).body
        return model_version_to_mlflow_obj(body.model_version)

    @catch_api_exceptions
    def get_model_version_download_uri(self, name, version):
        body = self.client.get_model_version_download_uri(
            GetModelVersionDownloadUriRequest(name, version)
        ).body
        return body.artifact_uri

    @catch_api_exceptions
    def search_model_versions(self, filter_string):
        body = self.client.search_model_versions(
            SearchModelVersionsRequest(filter_string)
        ).body
        return PagedList(
            [model_version_to_mlflow_obj(i) for i in body.model_versions]
            if body.model_versions
            else [],
            body.next_page_token,
        )

    @catch_api_exceptions
    def set_model_version_tag(self, name, version, tag):
        self.client.set_model_version_tag(
            SetModelVersionTagRequest(name, version, tag.key, tag.value)
        )

    @catch_api_exceptions
    def delete_model_version_tag(self, name, version, key):
        self.client.delete_model_version_tag(
            DeleteModelVersionTagRequest(name, version, key)
        )
