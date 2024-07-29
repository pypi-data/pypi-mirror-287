# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from pai_mlflow.vendor.alibabacloud_mlflow20210312 import models as mlflow_20210312_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('mlflow', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_model_version(
        self,
        request: mlflow_20210312_models.CreateModelVersionRequest,
    ) -> mlflow_20210312_models.CreateModelVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_model_version_with_options(request, headers, runtime)

    async def create_model_version_async(
        self,
        request: mlflow_20210312_models.CreateModelVersionRequest,
    ) -> mlflow_20210312_models.CreateModelVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_model_version_with_options_async(request, headers, runtime)

    def create_model_version_with_options(
        self,
        request: mlflow_20210312_models.CreateModelVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.CreateModelVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.run_link):
            body['run_link'] = request.run_link
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.CreateModelVersionResponse().from_map(
            self.do_roarequest('CreateModelVersion', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/preview/mlflow/model-versions/create', 'json', req, runtime)
        )

    async def create_model_version_with_options_async(
        self,
        request: mlflow_20210312_models.CreateModelVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.CreateModelVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.run_link):
            body['run_link'] = request.run_link
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.CreateModelVersionResponse().from_map(
            await self.do_roarequest_async('CreateModelVersion', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/preview/mlflow/model-versions/create', 'json', req, runtime)
        )

    def create_experiment(
        self,
        request: mlflow_20210312_models.CreateExperimentRequest,
    ) -> mlflow_20210312_models.CreateExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_experiment_with_options(request, headers, runtime)

    async def create_experiment_async(
        self,
        request: mlflow_20210312_models.CreateExperimentRequest,
    ) -> mlflow_20210312_models.CreateExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_experiment_with_options_async(request, headers, runtime)

    def create_experiment_with_options(
        self,
        request: mlflow_20210312_models.CreateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.CreateExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.artifact_location):
            body['artifact_location'] = request.artifact_location
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.CreateExperimentResponse().from_map(
            self.do_roarequest('CreateExperiment', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/experiments/create', 'json', req, runtime)
        )

    async def create_experiment_with_options_async(
        self,
        request: mlflow_20210312_models.CreateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.CreateExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.artifact_location):
            body['artifact_location'] = request.artifact_location
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.CreateExperimentResponse().from_map(
            await self.do_roarequest_async('CreateExperiment', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/experiments/create', 'json', req, runtime)
        )

    def log_model(
        self,
        request: mlflow_20210312_models.LogModelRequest,
    ) -> mlflow_20210312_models.LogModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.log_model_with_options(request, headers, runtime)

    async def log_model_async(
        self,
        request: mlflow_20210312_models.LogModelRequest,
    ) -> mlflow_20210312_models.LogModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.log_model_with_options_async(request, headers, runtime)

    def log_model_with_options(
        self,
        request: mlflow_20210312_models.LogModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.LogModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.model_json):
            body['model_json'] = request.model_json
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.LogModelResponse().from_map(
            self.do_roarequest('LogModel', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/log-model', 'none', req, runtime)
        )

    async def log_model_with_options_async(
        self,
        request: mlflow_20210312_models.LogModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.LogModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.model_json):
            body['model_json'] = request.model_json
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.LogModelResponse().from_map(
            await self.do_roarequest_async('LogModel', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/log-model', 'none', req, runtime)
        )

    def search_model_versions(
        self,
        request: mlflow_20210312_models.SearchModelVersionsRequest,
    ) -> mlflow_20210312_models.SearchModelVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_model_versions_with_options(request, headers, runtime)

    async def search_model_versions_async(
        self,
        request: mlflow_20210312_models.SearchModelVersionsRequest,
    ) -> mlflow_20210312_models.SearchModelVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_model_versions_with_options_async(request, headers, runtime)

    def search_model_versions_with_options(
        self,
        tmp_req: mlflow_20210312_models.SearchModelVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.SearchModelVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = mlflow_20210312_models.SearchModelVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_by):
            request.order_by_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_by, 'order_by', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['max_results'] = request.max_results
        if not UtilClient.is_unset(request.order_by_shrink):
            query['order_by'] = request.order_by_shrink
        if not UtilClient.is_unset(request.page_token):
            query['page_token'] = request.page_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.SearchModelVersionsResponse().from_map(
            self.do_roarequest('SearchModelVersions', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/preview/mlflow/model-versions/search', 'json', req, runtime)
        )

    async def search_model_versions_with_options_async(
        self,
        tmp_req: mlflow_20210312_models.SearchModelVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.SearchModelVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = mlflow_20210312_models.SearchModelVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_by):
            request.order_by_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_by, 'order_by', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['max_results'] = request.max_results
        if not UtilClient.is_unset(request.order_by_shrink):
            query['order_by'] = request.order_by_shrink
        if not UtilClient.is_unset(request.page_token):
            query['page_token'] = request.page_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.SearchModelVersionsResponse().from_map(
            await self.do_roarequest_async('SearchModelVersions', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/preview/mlflow/model-versions/search', 'json', req, runtime)
        )

    def search_runs(
        self,
        request: mlflow_20210312_models.SearchRunsRequest,
    ) -> mlflow_20210312_models.SearchRunsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_runs_with_options(request, headers, runtime)

    async def search_runs_async(
        self,
        request: mlflow_20210312_models.SearchRunsRequest,
    ) -> mlflow_20210312_models.SearchRunsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_runs_with_options_async(request, headers, runtime)

    def search_runs_with_options(
        self,
        request: mlflow_20210312_models.SearchRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.SearchRunsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.experiment_ids):
            body['experiment_ids'] = request.experiment_ids
        if not UtilClient.is_unset(request.filter):
            body['filter'] = request.filter
        if not UtilClient.is_unset(request.run_view_type):
            body['run_view_type'] = request.run_view_type
        if not UtilClient.is_unset(request.max_results):
            body['max_results'] = request.max_results
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.page_token):
            body['page_token'] = request.page_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.SearchRunsResponse().from_map(
            self.do_roarequest('SearchRuns', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/search', 'json', req, runtime)
        )

    async def search_runs_with_options_async(
        self,
        request: mlflow_20210312_models.SearchRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.SearchRunsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.experiment_ids):
            body['experiment_ids'] = request.experiment_ids
        if not UtilClient.is_unset(request.filter):
            body['filter'] = request.filter
        if not UtilClient.is_unset(request.run_view_type):
            body['run_view_type'] = request.run_view_type
        if not UtilClient.is_unset(request.max_results):
            body['max_results'] = request.max_results
        if not UtilClient.is_unset(request.order_by):
            body['order_by'] = request.order_by
        if not UtilClient.is_unset(request.page_token):
            body['page_token'] = request.page_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.SearchRunsResponse().from_map(
            await self.do_roarequest_async('SearchRuns', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/search', 'json', req, runtime)
        )

    def list_experiments(
        self,
        request: mlflow_20210312_models.ListExperimentsRequest,
    ) -> mlflow_20210312_models.ListExperimentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_experiments_with_options(request, headers, runtime)

    async def list_experiments_async(
        self,
        request: mlflow_20210312_models.ListExperimentsRequest,
    ) -> mlflow_20210312_models.ListExperimentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_experiments_with_options_async(request, headers, runtime)

    def list_experiments_with_options(
        self,
        request: mlflow_20210312_models.ListExperimentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.ListExperimentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.view_type):
            query['ViewType'] = request.view_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.ListExperimentsResponse().from_map(
            self.do_roarequest('ListExperiments', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/mlflow/experiments/list', 'json', req, runtime)
        )

    async def list_experiments_with_options_async(
        self,
        request: mlflow_20210312_models.ListExperimentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.ListExperimentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.view_type):
            query['ViewType'] = request.view_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.ListExperimentsResponse().from_map(
            await self.do_roarequest_async('ListExperiments', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/mlflow/experiments/list', 'json', req, runtime)
        )

    def set_experiment_tag(
        self,
        request: mlflow_20210312_models.SetExperimentTagRequest,
    ) -> mlflow_20210312_models.SetExperimentTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.set_experiment_tag_with_options(request, headers, runtime)

    async def set_experiment_tag_async(
        self,
        request: mlflow_20210312_models.SetExperimentTagRequest,
    ) -> mlflow_20210312_models.SetExperimentTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.set_experiment_tag_with_options_async(request, headers, runtime)

    def set_experiment_tag_with_options(
        self,
        request: mlflow_20210312_models.SetExperimentTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.SetExperimentTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.experiment_id):
            body['experiment_id'] = request.experiment_id
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.SetExperimentTagResponse().from_map(
            self.do_roarequest('SetExperimentTag', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/experiments/set-experiment-tag', 'none', req, runtime)
        )

    async def set_experiment_tag_with_options_async(
        self,
        request: mlflow_20210312_models.SetExperimentTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.SetExperimentTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.experiment_id):
            body['experiment_id'] = request.experiment_id
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.SetExperimentTagResponse().from_map(
            await self.do_roarequest_async('SetExperimentTag', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/experiments/set-experiment-tag', 'none', req, runtime)
        )

    def log_param(
        self,
        request: mlflow_20210312_models.LogParamRequest,
    ) -> mlflow_20210312_models.LogParamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.log_param_with_options(request, headers, runtime)

    async def log_param_async(
        self,
        request: mlflow_20210312_models.LogParamRequest,
    ) -> mlflow_20210312_models.LogParamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.log_param_with_options_async(request, headers, runtime)

    def log_param_with_options(
        self,
        request: mlflow_20210312_models.LogParamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.LogParamResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.LogParamResponse().from_map(
            self.do_roarequest('LogParam', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/log-parameter', 'none', req, runtime)
        )

    async def log_param_with_options_async(
        self,
        request: mlflow_20210312_models.LogParamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.LogParamResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.LogParamResponse().from_map(
            await self.do_roarequest_async('LogParam', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/log-parameter', 'none', req, runtime)
        )

    def get_latest_versions(
        self,
        request: mlflow_20210312_models.GetLatestVersionsRequest,
    ) -> mlflow_20210312_models.GetLatestVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_latest_versions_with_options(request, headers, runtime)

    async def get_latest_versions_async(
        self,
        request: mlflow_20210312_models.GetLatestVersionsRequest,
    ) -> mlflow_20210312_models.GetLatestVersionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_latest_versions_with_options_async(request, headers, runtime)

    def get_latest_versions_with_options(
        self,
        tmp_req: mlflow_20210312_models.GetLatestVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetLatestVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = mlflow_20210312_models.GetLatestVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stages):
            request.stages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stages, 'stages', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.stages_shrink):
            query['stages'] = request.stages_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetLatestVersionsResponse().from_map(
            self.do_roarequest('GetLatestVersions', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/preview/mlflow/registered-models/get-latest-versions', 'json', req, runtime)
        )

    async def get_latest_versions_with_options_async(
        self,
        tmp_req: mlflow_20210312_models.GetLatestVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetLatestVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = mlflow_20210312_models.GetLatestVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stages):
            request.stages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stages, 'stages', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.stages_shrink):
            query['stages'] = request.stages_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetLatestVersionsResponse().from_map(
            await self.do_roarequest_async('GetLatestVersions', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/preview/mlflow/registered-models/get-latest-versions', 'json', req, runtime)
        )

    def transition_model_version_stage(
        self,
        request: mlflow_20210312_models.TransitionModelVersionStageRequest,
    ) -> mlflow_20210312_models.TransitionModelVersionStageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.transition_model_version_stage_with_options(request, headers, runtime)

    async def transition_model_version_stage_async(
        self,
        request: mlflow_20210312_models.TransitionModelVersionStageRequest,
    ) -> mlflow_20210312_models.TransitionModelVersionStageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.transition_model_version_stage_with_options_async(request, headers, runtime)

    def transition_model_version_stage_with_options(
        self,
        request: mlflow_20210312_models.TransitionModelVersionStageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.TransitionModelVersionStageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.stage):
            body['stage'] = request.stage
        if not UtilClient.is_unset(request.archive_existing_versions):
            body['archive_existing_versions'] = request.archive_existing_versions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.TransitionModelVersionStageResponse().from_map(
            self.do_roarequest('TransitionModelVersionStage', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/preview/mlflow/model-versions/transition-stage', 'json', req, runtime)
        )

    async def transition_model_version_stage_with_options_async(
        self,
        request: mlflow_20210312_models.TransitionModelVersionStageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.TransitionModelVersionStageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.stage):
            body['stage'] = request.stage
        if not UtilClient.is_unset(request.archive_existing_versions):
            body['archive_existing_versions'] = request.archive_existing_versions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.TransitionModelVersionStageResponse().from_map(
            await self.do_roarequest_async('TransitionModelVersionStage', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/preview/mlflow/model-versions/transition-stage', 'json', req, runtime)
        )

    def rename_registered_model(
        self,
        request: mlflow_20210312_models.RenameRegisteredModelRequest,
    ) -> mlflow_20210312_models.RenameRegisteredModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rename_registered_model_with_options(request, headers, runtime)

    async def rename_registered_model_async(
        self,
        request: mlflow_20210312_models.RenameRegisteredModelRequest,
    ) -> mlflow_20210312_models.RenameRegisteredModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rename_registered_model_with_options_async(request, headers, runtime)

    def rename_registered_model_with_options(
        self,
        request: mlflow_20210312_models.RenameRegisteredModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.RenameRegisteredModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.new_name):
            body['new_name'] = request.new_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.RenameRegisteredModelResponse().from_map(
            self.do_roarequest('RenameRegisteredModel', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/preview/mlflow/registered-models/rename', 'json', req, runtime)
        )

    async def rename_registered_model_with_options_async(
        self,
        request: mlflow_20210312_models.RenameRegisteredModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.RenameRegisteredModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.new_name):
            body['new_name'] = request.new_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.RenameRegisteredModelResponse().from_map(
            await self.do_roarequest_async('RenameRegisteredModel', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/preview/mlflow/registered-models/rename', 'json', req, runtime)
        )

    def delete_run(
        self,
        request: mlflow_20210312_models.DeleteRunRequest,
    ) -> mlflow_20210312_models.DeleteRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_run_with_options(request, headers, runtime)

    async def delete_run_async(
        self,
        request: mlflow_20210312_models.DeleteRunRequest,
    ) -> mlflow_20210312_models.DeleteRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_run_with_options_async(request, headers, runtime)

    def delete_run_with_options(
        self,
        request: mlflow_20210312_models.DeleteRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.DeleteRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.DeleteRunResponse().from_map(
            self.do_roarequest('DeleteRun', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/delete', 'none', req, runtime)
        )

    async def delete_run_with_options_async(
        self,
        request: mlflow_20210312_models.DeleteRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.DeleteRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.DeleteRunResponse().from_map(
            await self.do_roarequest_async('DeleteRun', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/delete', 'none', req, runtime)
        )

    def create_run(
        self,
        request: mlflow_20210312_models.CreateRunRequest,
    ) -> mlflow_20210312_models.CreateRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_run_with_options(request, headers, runtime)

    async def create_run_async(
        self,
        request: mlflow_20210312_models.CreateRunRequest,
    ) -> mlflow_20210312_models.CreateRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_run_with_options_async(request, headers, runtime)

    def create_run_with_options(
        self,
        request: mlflow_20210312_models.CreateRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.CreateRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.experiment_id):
            body['experiment_id'] = request.experiment_id
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.start_time):
            body['start_time'] = request.start_time
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.CreateRunResponse().from_map(
            self.do_roarequest('CreateRun', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/create', 'json', req, runtime)
        )

    async def create_run_with_options_async(
        self,
        request: mlflow_20210312_models.CreateRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.CreateRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.experiment_id):
            body['experiment_id'] = request.experiment_id
        if not UtilClient.is_unset(request.user_id):
            body['user_id'] = request.user_id
        if not UtilClient.is_unset(request.start_time):
            body['start_time'] = request.start_time
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.CreateRunResponse().from_map(
            await self.do_roarequest_async('CreateRun', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/create', 'json', req, runtime)
        )

    def delete_model_version_tag(
        self,
        request: mlflow_20210312_models.DeleteModelVersionTagRequest,
    ) -> mlflow_20210312_models.DeleteModelVersionTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_model_version_tag_with_options(request, headers, runtime)

    async def delete_model_version_tag_async(
        self,
        request: mlflow_20210312_models.DeleteModelVersionTagRequest,
    ) -> mlflow_20210312_models.DeleteModelVersionTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_model_version_tag_with_options_async(request, headers, runtime)

    def delete_model_version_tag_with_options(
        self,
        request: mlflow_20210312_models.DeleteModelVersionTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.DeleteModelVersionTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.DeleteModelVersionTagResponse().from_map(
            self.do_roarequest('DeleteModelVersionTag', '2021-03-12', 'HTTPS', 'DELETE', 'AK', f'/api/2.0/preview/mlflow/model-versions/delete-tag', 'none', req, runtime)
        )

    async def delete_model_version_tag_with_options_async(
        self,
        request: mlflow_20210312_models.DeleteModelVersionTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.DeleteModelVersionTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.DeleteModelVersionTagResponse().from_map(
            await self.do_roarequest_async('DeleteModelVersionTag', '2021-03-12', 'HTTPS', 'DELETE', 'AK', f'/api/2.0/preview/mlflow/model-versions/delete-tag', 'none', req, runtime)
        )

    def get_registered_model(
        self,
        request: mlflow_20210312_models.GetRegisteredModelRequest,
    ) -> mlflow_20210312_models.GetRegisteredModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_registered_model_with_options(request, headers, runtime)

    async def get_registered_model_async(
        self,
        request: mlflow_20210312_models.GetRegisteredModelRequest,
    ) -> mlflow_20210312_models.GetRegisteredModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_registered_model_with_options_async(request, headers, runtime)

    def get_registered_model_with_options(
        self,
        request: mlflow_20210312_models.GetRegisteredModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetRegisteredModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetRegisteredModelResponse().from_map(
            self.do_roarequest('GetRegisteredModel', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/preview/mlflow/registered-models/get', 'json', req, runtime)
        )

    async def get_registered_model_with_options_async(
        self,
        request: mlflow_20210312_models.GetRegisteredModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetRegisteredModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetRegisteredModelResponse().from_map(
            await self.do_roarequest_async('GetRegisteredModel', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/preview/mlflow/registered-models/get', 'json', req, runtime)
        )

    def get_run(
        self,
        request: mlflow_20210312_models.GetRunRequest,
    ) -> mlflow_20210312_models.GetRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_run_with_options(request, headers, runtime)

    async def get_run_async(
        self,
        request: mlflow_20210312_models.GetRunRequest,
    ) -> mlflow_20210312_models.GetRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_run_with_options_async(request, headers, runtime)

    def get_run_with_options(
        self,
        request: mlflow_20210312_models.GetRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetRunResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.run_id):
            query['run_id'] = request.run_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetRunResponse().from_map(
            self.do_roarequest('GetRun', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/mlflow/runs/get', 'json', req, runtime)
        )

    async def get_run_with_options_async(
        self,
        request: mlflow_20210312_models.GetRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetRunResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.run_id):
            query['run_id'] = request.run_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetRunResponse().from_map(
            await self.do_roarequest_async('GetRun', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/mlflow/runs/get', 'json', req, runtime)
        )

    def get_metric_history(
        self,
        request: mlflow_20210312_models.GetMetricHistoryRequest,
    ) -> mlflow_20210312_models.GetMetricHistoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_metric_history_with_options(request, headers, runtime)

    async def get_metric_history_async(
        self,
        request: mlflow_20210312_models.GetMetricHistoryRequest,
    ) -> mlflow_20210312_models.GetMetricHistoryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_metric_history_with_options_async(request, headers, runtime)

    def get_metric_history_with_options(
        self,
        request: mlflow_20210312_models.GetMetricHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetMetricHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.run_id):
            query['run_id'] = request.run_id
        if not UtilClient.is_unset(request.metric_key):
            query['metric_key'] = request.metric_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetMetricHistoryResponse().from_map(
            self.do_roarequest('GetMetricHistory', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/mlflow/metrics/get-history', 'json', req, runtime)
        )

    async def get_metric_history_with_options_async(
        self,
        request: mlflow_20210312_models.GetMetricHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetMetricHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.run_id):
            query['run_id'] = request.run_id
        if not UtilClient.is_unset(request.metric_key):
            query['metric_key'] = request.metric_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetMetricHistoryResponse().from_map(
            await self.do_roarequest_async('GetMetricHistory', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/mlflow/metrics/get-history', 'json', req, runtime)
        )

    def get_experiment(
        self,
        request: mlflow_20210312_models.GetExperimentRequest,
    ) -> mlflow_20210312_models.GetExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_with_options(request, headers, runtime)

    async def get_experiment_async(
        self,
        request: mlflow_20210312_models.GetExperimentRequest,
    ) -> mlflow_20210312_models.GetExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_experiment_with_options_async(request, headers, runtime)

    def get_experiment_with_options(
        self,
        request: mlflow_20210312_models.GetExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetExperimentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['experiment_id'] = request.experiment_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetExperimentResponse().from_map(
            self.do_roarequest('GetExperiment', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/mlflow/experiments/get', 'json', req, runtime)
        )

    async def get_experiment_with_options_async(
        self,
        request: mlflow_20210312_models.GetExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetExperimentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['experiment_id'] = request.experiment_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetExperimentResponse().from_map(
            await self.do_roarequest_async('GetExperiment', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/mlflow/experiments/get', 'json', req, runtime)
        )

    def search_registered_models(
        self,
        request: mlflow_20210312_models.SearchRegisteredModelsRequest,
    ) -> mlflow_20210312_models.SearchRegisteredModelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_registered_models_with_options(request, headers, runtime)

    async def search_registered_models_async(
        self,
        request: mlflow_20210312_models.SearchRegisteredModelsRequest,
    ) -> mlflow_20210312_models.SearchRegisteredModelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_registered_models_with_options_async(request, headers, runtime)

    def search_registered_models_with_options(
        self,
        tmp_req: mlflow_20210312_models.SearchRegisteredModelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.SearchRegisteredModelsResponse:
        UtilClient.validate_model(tmp_req)
        request = mlflow_20210312_models.SearchRegisteredModelsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_by):
            request.order_by_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_by, 'order_by', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['max_results'] = request.max_results
        if not UtilClient.is_unset(request.order_by_shrink):
            query['order_by'] = request.order_by_shrink
        if not UtilClient.is_unset(request.page_token):
            query['page_token'] = request.page_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.SearchRegisteredModelsResponse().from_map(
            self.do_roarequest('SearchRegisteredModels', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/preview/mlflow/registered-models/search', 'json', req, runtime)
        )

    async def search_registered_models_with_options_async(
        self,
        tmp_req: mlflow_20210312_models.SearchRegisteredModelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.SearchRegisteredModelsResponse:
        UtilClient.validate_model(tmp_req)
        request = mlflow_20210312_models.SearchRegisteredModelsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_by):
            request.order_by_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_by, 'order_by', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['max_results'] = request.max_results
        if not UtilClient.is_unset(request.order_by_shrink):
            query['order_by'] = request.order_by_shrink
        if not UtilClient.is_unset(request.page_token):
            query['page_token'] = request.page_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.SearchRegisteredModelsResponse().from_map(
            await self.do_roarequest_async('SearchRegisteredModels', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/preview/mlflow/registered-models/search', 'json', req, runtime)
        )

    def update_registered_model(
        self,
        request: mlflow_20210312_models.UpdateRegisteredModelRequest,
    ) -> mlflow_20210312_models.UpdateRegisteredModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_registered_model_with_options(request, headers, runtime)

    async def update_registered_model_async(
        self,
        request: mlflow_20210312_models.UpdateRegisteredModelRequest,
    ) -> mlflow_20210312_models.UpdateRegisteredModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_registered_model_with_options_async(request, headers, runtime)

    def update_registered_model_with_options(
        self,
        request: mlflow_20210312_models.UpdateRegisteredModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.UpdateRegisteredModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.UpdateRegisteredModelResponse().from_map(
            self.do_roarequest('UpdateRegisteredModel', '2021-03-12', 'HTTPS', 'PATCH', 'AK', f'/api/2.0/preview/mlflow/registered-models/update', 'json', req, runtime)
        )

    async def update_registered_model_with_options_async(
        self,
        request: mlflow_20210312_models.UpdateRegisteredModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.UpdateRegisteredModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.UpdateRegisteredModelResponse().from_map(
            await self.do_roarequest_async('UpdateRegisteredModel', '2021-03-12', 'HTTPS', 'PATCH', 'AK', f'/api/2.0/preview/mlflow/registered-models/update', 'json', req, runtime)
        )

    def delete_model_version(
        self,
        request: mlflow_20210312_models.DeleteModelVersionRequest,
    ) -> mlflow_20210312_models.DeleteModelVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_model_version_with_options(request, headers, runtime)

    async def delete_model_version_async(
        self,
        request: mlflow_20210312_models.DeleteModelVersionRequest,
    ) -> mlflow_20210312_models.DeleteModelVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_model_version_with_options_async(request, headers, runtime)

    def delete_model_version_with_options(
        self,
        request: mlflow_20210312_models.DeleteModelVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.DeleteModelVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.DeleteModelVersionResponse().from_map(
            self.do_roarequest('DeleteModelVersion', '2021-03-12', 'HTTPS', 'DELETE', 'AK', f'/api/2.0/preview/mlflow/model-versions/delete', 'none', req, runtime)
        )

    async def delete_model_version_with_options_async(
        self,
        request: mlflow_20210312_models.DeleteModelVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.DeleteModelVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.DeleteModelVersionResponse().from_map(
            await self.do_roarequest_async('DeleteModelVersion', '2021-03-12', 'HTTPS', 'DELETE', 'AK', f'/api/2.0/preview/mlflow/model-versions/delete', 'none', req, runtime)
        )

    def set_registered_model_tag(
        self,
        request: mlflow_20210312_models.SetRegisteredModelTagRequest,
    ) -> mlflow_20210312_models.SetRegisteredModelTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.set_registered_model_tag_with_options(request, headers, runtime)

    async def set_registered_model_tag_async(
        self,
        request: mlflow_20210312_models.SetRegisteredModelTagRequest,
    ) -> mlflow_20210312_models.SetRegisteredModelTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.set_registered_model_tag_with_options_async(request, headers, runtime)

    def set_registered_model_tag_with_options(
        self,
        request: mlflow_20210312_models.SetRegisteredModelTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.SetRegisteredModelTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.SetRegisteredModelTagResponse().from_map(
            self.do_roarequest('SetRegisteredModelTag', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/preview/mlflow/registered-models/set-tag', 'none', req, runtime)
        )

    async def set_registered_model_tag_with_options_async(
        self,
        request: mlflow_20210312_models.SetRegisteredModelTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.SetRegisteredModelTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.SetRegisteredModelTagResponse().from_map(
            await self.do_roarequest_async('SetRegisteredModelTag', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/preview/mlflow/registered-models/set-tag', 'none', req, runtime)
        )

    def set_tag(
        self,
        request: mlflow_20210312_models.SetTagRequest,
    ) -> mlflow_20210312_models.SetTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.set_tag_with_options(request, headers, runtime)

    async def set_tag_async(
        self,
        request: mlflow_20210312_models.SetTagRequest,
    ) -> mlflow_20210312_models.SetTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.set_tag_with_options_async(request, headers, runtime)

    def set_tag_with_options(
        self,
        request: mlflow_20210312_models.SetTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.SetTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.SetTagResponse().from_map(
            self.do_roarequest('SetTag', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/set-tag', 'none', req, runtime)
        )

    async def set_tag_with_options_async(
        self,
        request: mlflow_20210312_models.SetTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.SetTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.SetTagResponse().from_map(
            await self.do_roarequest_async('SetTag', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/set-tag', 'none', req, runtime)
        )

    def delete_tag(
        self,
        request: mlflow_20210312_models.DeleteTagRequest,
    ) -> mlflow_20210312_models.DeleteTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_tag_with_options(request, headers, runtime)

    async def delete_tag_async(
        self,
        request: mlflow_20210312_models.DeleteTagRequest,
    ) -> mlflow_20210312_models.DeleteTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_tag_with_options_async(request, headers, runtime)

    def delete_tag_with_options(
        self,
        request: mlflow_20210312_models.DeleteTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.DeleteTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.DeleteTagResponse().from_map(
            self.do_roarequest('DeleteTag', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/delete-tag', 'none', req, runtime)
        )

    async def delete_tag_with_options_async(
        self,
        request: mlflow_20210312_models.DeleteTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.DeleteTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.DeleteTagResponse().from_map(
            await self.do_roarequest_async('DeleteTag', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/delete-tag', 'none', req, runtime)
        )

    def list_registered_models(
        self,
        request: mlflow_20210312_models.ListRegisteredModelsRequest,
    ) -> mlflow_20210312_models.ListRegisteredModelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_registered_models_with_options(request, headers, runtime)

    async def list_registered_models_async(
        self,
        request: mlflow_20210312_models.ListRegisteredModelsRequest,
    ) -> mlflow_20210312_models.ListRegisteredModelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_registered_models_with_options_async(request, headers, runtime)

    def list_registered_models_with_options(
        self,
        request: mlflow_20210312_models.ListRegisteredModelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.ListRegisteredModelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['max_results'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['page_token'] = request.page_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.ListRegisteredModelsResponse().from_map(
            self.do_roarequest('ListRegisteredModels', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/preview/mlflow/registered-models/list', 'json', req, runtime)
        )

    async def list_registered_models_with_options_async(
        self,
        request: mlflow_20210312_models.ListRegisteredModelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.ListRegisteredModelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['max_results'] = request.max_results
        if not UtilClient.is_unset(request.page_token):
            query['page_token'] = request.page_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.ListRegisteredModelsResponse().from_map(
            await self.do_roarequest_async('ListRegisteredModels', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/preview/mlflow/registered-models/list', 'json', req, runtime)
        )

    def update_run(
        self,
        request: mlflow_20210312_models.UpdateRunRequest,
    ) -> mlflow_20210312_models.UpdateRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_run_with_options(request, headers, runtime)

    async def update_run_async(
        self,
        request: mlflow_20210312_models.UpdateRunRequest,
    ) -> mlflow_20210312_models.UpdateRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_run_with_options_async(request, headers, runtime)

    def update_run_with_options(
        self,
        request: mlflow_20210312_models.UpdateRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.UpdateRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.end_time):
            body['end_time'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.UpdateRunResponse().from_map(
            self.do_roarequest('UpdateRun', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/update', 'json', req, runtime)
        )

    async def update_run_with_options_async(
        self,
        request: mlflow_20210312_models.UpdateRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.UpdateRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.end_time):
            body['end_time'] = request.end_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.UpdateRunResponse().from_map(
            await self.do_roarequest_async('UpdateRun', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/update', 'json', req, runtime)
        )

    def restore_run(
        self,
        request: mlflow_20210312_models.RestoreRunRequest,
    ) -> mlflow_20210312_models.RestoreRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restore_run_with_options(request, headers, runtime)

    async def restore_run_async(
        self,
        request: mlflow_20210312_models.RestoreRunRequest,
    ) -> mlflow_20210312_models.RestoreRunResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restore_run_with_options_async(request, headers, runtime)

    def restore_run_with_options(
        self,
        request: mlflow_20210312_models.RestoreRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.RestoreRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.RestoreRunResponse().from_map(
            self.do_roarequest('RestoreRun', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/restore', 'none', req, runtime)
        )

    async def restore_run_with_options_async(
        self,
        request: mlflow_20210312_models.RestoreRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.RestoreRunResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.RestoreRunResponse().from_map(
            await self.do_roarequest_async('RestoreRun', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/restore', 'none', req, runtime)
        )

    def create_registered_model(
        self,
        request: mlflow_20210312_models.CreateRegisteredModelRequest,
    ) -> mlflow_20210312_models.CreateRegisteredModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_registered_model_with_options(request, headers, runtime)

    async def create_registered_model_async(
        self,
        request: mlflow_20210312_models.CreateRegisteredModelRequest,
    ) -> mlflow_20210312_models.CreateRegisteredModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_registered_model_with_options_async(request, headers, runtime)

    def create_registered_model_with_options(
        self,
        request: mlflow_20210312_models.CreateRegisteredModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.CreateRegisteredModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.CreateRegisteredModelResponse().from_map(
            self.do_roarequest('CreateRegisteredModel', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/preview/mlflow/registered-models/create', 'json', req, runtime)
        )

    async def create_registered_model_with_options_async(
        self,
        request: mlflow_20210312_models.CreateRegisteredModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.CreateRegisteredModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.CreateRegisteredModelResponse().from_map(
            await self.do_roarequest_async('CreateRegisteredModel', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/preview/mlflow/registered-models/create', 'json', req, runtime)
        )

    def set_model_version_tag(
        self,
        request: mlflow_20210312_models.SetModelVersionTagRequest,
    ) -> mlflow_20210312_models.SetModelVersionTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.set_model_version_tag_with_options(request, headers, runtime)

    async def set_model_version_tag_async(
        self,
        request: mlflow_20210312_models.SetModelVersionTagRequest,
    ) -> mlflow_20210312_models.SetModelVersionTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.set_model_version_tag_with_options_async(request, headers, runtime)

    def set_model_version_tag_with_options(
        self,
        request: mlflow_20210312_models.SetModelVersionTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.SetModelVersionTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.SetModelVersionTagResponse().from_map(
            self.do_roarequest('SetModelVersionTag', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/preview/mlflow/model-versions/set-tag', 'none', req, runtime)
        )

    async def set_model_version_tag_with_options_async(
        self,
        request: mlflow_20210312_models.SetModelVersionTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.SetModelVersionTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.SetModelVersionTagResponse().from_map(
            await self.do_roarequest_async('SetModelVersionTag', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/preview/mlflow/model-versions/set-tag', 'none', req, runtime)
        )

    def get_experiment_by_name(
        self,
        request: mlflow_20210312_models.GetExperimentByNameRequest,
    ) -> mlflow_20210312_models.GetExperimentByNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_by_name_with_options(request, headers, runtime)

    async def get_experiment_by_name_async(
        self,
        request: mlflow_20210312_models.GetExperimentByNameRequest,
    ) -> mlflow_20210312_models.GetExperimentByNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_experiment_by_name_with_options_async(request, headers, runtime)

    def get_experiment_by_name_with_options(
        self,
        request: mlflow_20210312_models.GetExperimentByNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetExperimentByNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_name):
            query['experiment_name'] = request.experiment_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetExperimentByNameResponse().from_map(
            self.do_roarequest('GetExperimentByName', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/mlflow/experiments/get-by-name', 'json', req, runtime)
        )

    async def get_experiment_by_name_with_options_async(
        self,
        request: mlflow_20210312_models.GetExperimentByNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetExperimentByNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_name):
            query['experiment_name'] = request.experiment_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetExperimentByNameResponse().from_map(
            await self.do_roarequest_async('GetExperimentByName', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/mlflow/experiments/get-by-name', 'json', req, runtime)
        )

    def get_model_version(
        self,
        request: mlflow_20210312_models.GetModelVersionRequest,
    ) -> mlflow_20210312_models.GetModelVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_version_with_options(request, headers, runtime)

    async def get_model_version_async(
        self,
        request: mlflow_20210312_models.GetModelVersionRequest,
    ) -> mlflow_20210312_models.GetModelVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_model_version_with_options_async(request, headers, runtime)

    def get_model_version_with_options(
        self,
        request: mlflow_20210312_models.GetModelVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetModelVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetModelVersionResponse().from_map(
            self.do_roarequest('GetModelVersion', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/preview/mlflow/model-versions/get', 'json', req, runtime)
        )

    async def get_model_version_with_options_async(
        self,
        request: mlflow_20210312_models.GetModelVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetModelVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetModelVersionResponse().from_map(
            await self.do_roarequest_async('GetModelVersion', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/preview/mlflow/model-versions/get', 'json', req, runtime)
        )

    def restore_experiment(
        self,
        request: mlflow_20210312_models.RestoreExperimentRequest,
    ) -> mlflow_20210312_models.RestoreExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restore_experiment_with_options(request, headers, runtime)

    async def restore_experiment_async(
        self,
        request: mlflow_20210312_models.RestoreExperimentRequest,
    ) -> mlflow_20210312_models.RestoreExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restore_experiment_with_options_async(request, headers, runtime)

    def restore_experiment_with_options(
        self,
        request: mlflow_20210312_models.RestoreExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.RestoreExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.experiment_id):
            body['experiment_id'] = request.experiment_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.RestoreExperimentResponse().from_map(
            self.do_roarequest('RestoreExperiment', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/experiments/restore', 'none', req, runtime)
        )

    async def restore_experiment_with_options_async(
        self,
        request: mlflow_20210312_models.RestoreExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.RestoreExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.experiment_id):
            body['experiment_id'] = request.experiment_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.RestoreExperimentResponse().from_map(
            await self.do_roarequest_async('RestoreExperiment', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/experiments/restore', 'none', req, runtime)
        )

    def update_experiment(
        self,
        request: mlflow_20210312_models.UpdateExperimentRequest,
    ) -> mlflow_20210312_models.UpdateExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_with_options(request, headers, runtime)

    async def update_experiment_async(
        self,
        request: mlflow_20210312_models.UpdateExperimentRequest,
    ) -> mlflow_20210312_models.UpdateExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_experiment_with_options_async(request, headers, runtime)

    def update_experiment_with_options(
        self,
        request: mlflow_20210312_models.UpdateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.UpdateExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_name):
            body['new_name'] = request.new_name
        if not UtilClient.is_unset(request.experiment_id):
            body['experiment_id'] = request.experiment_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.UpdateExperimentResponse().from_map(
            self.do_roarequest('UpdateExperiment', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/experiments/update', 'none', req, runtime)
        )

    async def update_experiment_with_options_async(
        self,
        request: mlflow_20210312_models.UpdateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.UpdateExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_name):
            body['new_name'] = request.new_name
        if not UtilClient.is_unset(request.experiment_id):
            body['experiment_id'] = request.experiment_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.UpdateExperimentResponse().from_map(
            await self.do_roarequest_async('UpdateExperiment', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/experiments/update', 'none', req, runtime)
        )

    def delete_registered_model_tag(
        self,
        request: mlflow_20210312_models.DeleteRegisteredModelTagRequest,
    ) -> mlflow_20210312_models.DeleteRegisteredModelTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_registered_model_tag_with_options(request, headers, runtime)

    async def delete_registered_model_tag_async(
        self,
        request: mlflow_20210312_models.DeleteRegisteredModelTagRequest,
    ) -> mlflow_20210312_models.DeleteRegisteredModelTagResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_registered_model_tag_with_options_async(request, headers, runtime)

    def delete_registered_model_tag_with_options(
        self,
        request: mlflow_20210312_models.DeleteRegisteredModelTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.DeleteRegisteredModelTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.DeleteRegisteredModelTagResponse().from_map(
            self.do_roarequest('DeleteRegisteredModelTag', '2021-03-12', 'HTTPS', 'DELETE', 'AK', f'/api/2.0/preview/mlflow/registered-models/delete-tag', 'none', req, runtime)
        )

    async def delete_registered_model_tag_with_options_async(
        self,
        request: mlflow_20210312_models.DeleteRegisteredModelTagRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.DeleteRegisteredModelTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.key):
            query['key'] = request.key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.DeleteRegisteredModelTagResponse().from_map(
            await self.do_roarequest_async('DeleteRegisteredModelTag', '2021-03-12', 'HTTPS', 'DELETE', 'AK', f'/api/2.0/preview/mlflow/registered-models/delete-tag', 'none', req, runtime)
        )

    def delete_experiment(
        self,
        request: mlflow_20210312_models.DeleteExperimentRequest,
    ) -> mlflow_20210312_models.DeleteExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_with_options(request, headers, runtime)

    async def delete_experiment_async(
        self,
        request: mlflow_20210312_models.DeleteExperimentRequest,
    ) -> mlflow_20210312_models.DeleteExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_experiment_with_options_async(request, headers, runtime)

    def delete_experiment_with_options(
        self,
        request: mlflow_20210312_models.DeleteExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.DeleteExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.experiment_id):
            body['experiment_id'] = request.experiment_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.DeleteExperimentResponse().from_map(
            self.do_roarequest('DeleteExperiment', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/experiments/delete', 'none', req, runtime)
        )

    async def delete_experiment_with_options_async(
        self,
        request: mlflow_20210312_models.DeleteExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.DeleteExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.experiment_id):
            body['experiment_id'] = request.experiment_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.DeleteExperimentResponse().from_map(
            await self.do_roarequest_async('DeleteExperiment', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/experiments/delete', 'none', req, runtime)
        )

    def get_model_version_download_uri(
        self,
        request: mlflow_20210312_models.GetModelVersionDownloadUriRequest,
    ) -> mlflow_20210312_models.GetModelVersionDownloadUriResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_version_download_uri_with_options(request, headers, runtime)

    async def get_model_version_download_uri_async(
        self,
        request: mlflow_20210312_models.GetModelVersionDownloadUriRequest,
    ) -> mlflow_20210312_models.GetModelVersionDownloadUriResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_model_version_download_uri_with_options_async(request, headers, runtime)

    def get_model_version_download_uri_with_options(
        self,
        request: mlflow_20210312_models.GetModelVersionDownloadUriRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetModelVersionDownloadUriResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetModelVersionDownloadUriResponse().from_map(
            self.do_roarequest('GetModelVersionDownloadUri', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/preview/mlflow/model-versions/get-download-uri', 'json', req, runtime)
        )

    async def get_model_version_download_uri_with_options_async(
        self,
        request: mlflow_20210312_models.GetModelVersionDownloadUriRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.GetModelVersionDownloadUriResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.GetModelVersionDownloadUriResponse().from_map(
            await self.do_roarequest_async('GetModelVersionDownloadUri', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/preview/mlflow/model-versions/get-download-uri', 'json', req, runtime)
        )

    def log_metric(
        self,
        request: mlflow_20210312_models.LogMetricRequest,
    ) -> mlflow_20210312_models.LogMetricResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.log_metric_with_options(request, headers, runtime)

    async def log_metric_async(
        self,
        request: mlflow_20210312_models.LogMetricRequest,
    ) -> mlflow_20210312_models.LogMetricResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.log_metric_with_options_async(request, headers, runtime)

    def log_metric_with_options(
        self,
        request: mlflow_20210312_models.LogMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.LogMetricResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.step):
            body['step'] = request.step
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.LogMetricResponse().from_map(
            self.do_roarequest('LogMetric', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/log-metric', 'none', req, runtime)
        )

    async def log_metric_with_options_async(
        self,
        request: mlflow_20210312_models.LogMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.LogMetricResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.key):
            body['key'] = request.key
        if not UtilClient.is_unset(request.value):
            body['value'] = request.value
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.step):
            body['step'] = request.step
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.LogMetricResponse().from_map(
            await self.do_roarequest_async('LogMetric', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/log-metric', 'none', req, runtime)
        )

    def list_artifacts(
        self,
        request: mlflow_20210312_models.ListArtifactsRequest,
    ) -> mlflow_20210312_models.ListArtifactsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_artifacts_with_options(request, headers, runtime)

    async def list_artifacts_async(
        self,
        request: mlflow_20210312_models.ListArtifactsRequest,
    ) -> mlflow_20210312_models.ListArtifactsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_artifacts_with_options_async(request, headers, runtime)

    def list_artifacts_with_options(
        self,
        request: mlflow_20210312_models.ListArtifactsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.ListArtifactsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.run_id):
            query['run_id'] = request.run_id
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.page_token):
            query['page_token'] = request.page_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.ListArtifactsResponse().from_map(
            self.do_roarequest('ListArtifacts', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/mlflow/artifacts/list', 'json', req, runtime)
        )

    async def list_artifacts_with_options_async(
        self,
        request: mlflow_20210312_models.ListArtifactsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.ListArtifactsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.run_id):
            query['run_id'] = request.run_id
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.page_token):
            query['page_token'] = request.page_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.ListArtifactsResponse().from_map(
            await self.do_roarequest_async('ListArtifacts', '2021-03-12', 'HTTPS', 'GET', 'AK', f'/api/2.0/mlflow/artifacts/list', 'json', req, runtime)
        )

    def log_batch(
        self,
        request: mlflow_20210312_models.LogBatchRequest,
    ) -> mlflow_20210312_models.LogBatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.log_batch_with_options(request, headers, runtime)

    async def log_batch_async(
        self,
        request: mlflow_20210312_models.LogBatchRequest,
    ) -> mlflow_20210312_models.LogBatchResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.log_batch_with_options_async(request, headers, runtime)

    def log_batch_with_options(
        self,
        request: mlflow_20210312_models.LogBatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.LogBatchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.metrics):
            body['metrics'] = request.metrics
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.LogBatchResponse().from_map(
            self.do_roarequest('LogBatch', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/log-batch', 'none', req, runtime)
        )

    async def log_batch_with_options_async(
        self,
        request: mlflow_20210312_models.LogBatchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.LogBatchResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.run_id):
            body['run_id'] = request.run_id
        if not UtilClient.is_unset(request.metrics):
            body['metrics'] = request.metrics
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.LogBatchResponse().from_map(
            await self.do_roarequest_async('LogBatch', '2021-03-12', 'HTTPS', 'POST', 'AK', f'/api/2.0/mlflow/runs/log-batch', 'none', req, runtime)
        )

    def delete_registered_model(
        self,
        request: mlflow_20210312_models.DeleteRegisteredModelRequest,
    ) -> mlflow_20210312_models.DeleteRegisteredModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_registered_model_with_options(request, headers, runtime)

    async def delete_registered_model_async(
        self,
        request: mlflow_20210312_models.DeleteRegisteredModelRequest,
    ) -> mlflow_20210312_models.DeleteRegisteredModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_registered_model_with_options_async(request, headers, runtime)

    def delete_registered_model_with_options(
        self,
        request: mlflow_20210312_models.DeleteRegisteredModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.DeleteRegisteredModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.DeleteRegisteredModelResponse().from_map(
            self.do_roarequest('DeleteRegisteredModel', '2021-03-12', 'HTTPS', 'DELETE', 'AK', f'/api/2.0/preview/mlflow/registered-models/delete', 'none', req, runtime)
        )

    async def delete_registered_model_with_options_async(
        self,
        request: mlflow_20210312_models.DeleteRegisteredModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.DeleteRegisteredModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return mlflow_20210312_models.DeleteRegisteredModelResponse().from_map(
            await self.do_roarequest_async('DeleteRegisteredModel', '2021-03-12', 'HTTPS', 'DELETE', 'AK', f'/api/2.0/preview/mlflow/registered-models/delete', 'none', req, runtime)
        )

    def update_model_version(
        self,
        request: mlflow_20210312_models.UpdateModelVersionRequest,
    ) -> mlflow_20210312_models.UpdateModelVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_model_version_with_options(request, headers, runtime)

    async def update_model_version_async(
        self,
        request: mlflow_20210312_models.UpdateModelVersionRequest,
    ) -> mlflow_20210312_models.UpdateModelVersionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_model_version_with_options_async(request, headers, runtime)

    def update_model_version_with_options(
        self,
        request: mlflow_20210312_models.UpdateModelVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.UpdateModelVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.UpdateModelVersionResponse().from_map(
            self.do_roarequest('UpdateModelVersion', '2021-03-12', 'HTTPS', 'PATCH', 'AK', f'/api/2.0/preview/mlflow/model-versions/update', 'json', req, runtime)
        )

    async def update_model_version_with_options_async(
        self,
        request: mlflow_20210312_models.UpdateModelVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mlflow_20210312_models.UpdateModelVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return mlflow_20210312_models.UpdateModelVersionResponse().from_map(
            await self.do_roarequest_async('UpdateModelVersion', '2021-03-12', 'HTTPS', 'PATCH', 'AK', f'/api/2.0/preview/mlflow/model-versions/update', 'json', req, runtime)
        )
