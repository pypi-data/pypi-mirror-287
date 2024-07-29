# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class Metric(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: float = None,
        timestamp: int = None,
        step: int = None,
    ):
        # key
        self.key = key
        # value
        self.value = value
        # timestamp
        self.timestamp = timestamp
        # step
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.step is not None:
            result['step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('step') is not None:
            self.step = m.get('step')
        return self


class Param(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Key
        self.key = key
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class RunTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # tag key
        self.key = key
        # tag value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class RunData(TeaModel):
    def __init__(
        self,
        metrics: List[Metric] = None,
        params: List[Param] = None,
        tags: List[RunTag] = None,
    ):
        # Metrics
        self.metrics = metrics
        # Params
        self.params = params
        # Tags
        self.tags = tags

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()
        if self.params:
            for k in self.params:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['metrics'].append(k.to_map() if k else None)
        result['params'] = []
        if self.params is not None:
            for k in self.params:
                result['params'].append(k.to_map() if k else None)
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('metrics') is not None:
            for k in m.get('metrics'):
                temp_model = Metric()
                self.metrics.append(temp_model.from_map(k))
        self.params = []
        if m.get('params') is not None:
            for k in m.get('params'):
                temp_model = Param()
                self.params.append(temp_model.from_map(k))
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = RunTag()
                self.tags.append(temp_model.from_map(k))
        return self


class ExperimentTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Key
        self.key = key
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class Experiment(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        name: str = None,
        artifact_location: str = None,
        lifecycle_stage: str = None,
        last_update_time: int = None,
        creation_time: int = None,
        tags: List[ExperimentTag] = None,
    ):
        # Experiment Id
        self.experiment_id = experiment_id
        # Name
        self.name = name
        # Artifact Location
        self.artifact_location = artifact_location
        # Lifecycle Stage
        self.lifecycle_stage = lifecycle_stage
        # Last Update Time
        self.last_update_time = last_update_time
        # Creation Time
        self.creation_time = creation_time
        # Tags
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.experiment_id is not None:
            result['experiment_id'] = self.experiment_id
        if self.name is not None:
            result['name'] = self.name
        if self.artifact_location is not None:
            result['artifact_location'] = self.artifact_location
        if self.lifecycle_stage is not None:
            result['lifecycle_stage'] = self.lifecycle_stage
        if self.last_update_time is not None:
            result['last_update_time'] = self.last_update_time
        if self.creation_time is not None:
            result['creation_time'] = self.creation_time
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('experiment_id') is not None:
            self.experiment_id = m.get('experiment_id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('artifact_location') is not None:
            self.artifact_location = m.get('artifact_location')
        if m.get('lifecycle_stage') is not None:
            self.lifecycle_stage = m.get('lifecycle_stage')
        if m.get('last_update_time') is not None:
            self.last_update_time = m.get('last_update_time')
        if m.get('creation_time') is not None:
            self.creation_time = m.get('creation_time')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ExperimentTag()
                self.tags.append(temp_model.from_map(k))
        return self


class RunInfo(TeaModel):
    def __init__(
        self,
        run_id: str = None,
        run_uuid: str = None,
        experiment_id: str = None,
        user_id: str = None,
        status: str = None,
        start_time: int = None,
        end_time: int = None,
        artifact_uri: str = None,
        lifecycle_stage: str = None,
    ):
        # run id
        self.run_id = run_id
        # run uuid
        self.run_uuid = run_uuid
        # experiment id
        self.experiment_id = experiment_id
        # user id
        self.user_id = user_id
        # status
        self.status = status
        # start time
        self.start_time = start_time
        # end time
        self.end_time = end_time
        # artifact uri
        self.artifact_uri = artifact_uri
        # lifecycle stage
        self.lifecycle_stage = lifecycle_stage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.run_id is not None:
            result['run_id'] = self.run_id
        if self.run_uuid is not None:
            result['run_uuid'] = self.run_uuid
        if self.experiment_id is not None:
            result['experiment_id'] = self.experiment_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.status is not None:
            result['status'] = self.status
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.artifact_uri is not None:
            result['artifact_uri'] = self.artifact_uri
        if self.lifecycle_stage is not None:
            result['lifecycle_stage'] = self.lifecycle_stage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')
        if m.get('run_uuid') is not None:
            self.run_uuid = m.get('run_uuid')
        if m.get('experiment_id') is not None:
            self.experiment_id = m.get('experiment_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('artifact_uri') is not None:
            self.artifact_uri = m.get('artifact_uri')
        if m.get('lifecycle_stage') is not None:
            self.lifecycle_stage = m.get('lifecycle_stage')
        return self


class Run(TeaModel):
    def __init__(
        self,
        info: RunInfo = None,
        data: RunData = None,
    ):
        self.info = info
        self.data = data

    def validate(self):
        if self.info:
            self.info.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.info is not None:
            result['info'] = self.info.to_map()
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('info') is not None:
            temp_model = RunInfo()
            self.info = temp_model.from_map(m['info'])
        if m.get('data') is not None:
            temp_model = RunData()
            self.data = temp_model.from_map(m['data'])
        return self


class ModelVersionTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Key
        self.key = key
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class FileInfo(TeaModel):
    def __init__(
        self,
        path: str = None,
        is_dir: bool = None,
        file_size: int = None,
    ):
        # Path
        self.path = path
        # IsDir
        self.is_dir = is_dir
        # FileSize
        self.file_size = file_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.is_dir is not None:
            result['is_dir'] = self.is_dir
        if self.file_size is not None:
            result['file_size'] = self.file_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('is_dir') is not None:
            self.is_dir = m.get('is_dir')
        if m.get('file_size') is not None:
            self.file_size = m.get('file_size')
        return self


class RegisteredModelTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Key
        self.key = key
        # Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ModelVersion(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
        creation_timestamp: int = None,
        last_updated_timestamp: int = None,
        user_id: str = None,
        current_stage: str = None,
        description: str = None,
        source: str = None,
        run_id: str = None,
        status: str = None,
        status_message: str = None,
        tags: List[ModelVersionTag] = None,
        run_link: str = None,
    ):
        # Name
        self.name = name
        # Version
        self.version = version
        # CreationTimestamp
        self.creation_timestamp = creation_timestamp
        # LastUpdatedTimestamp
        self.last_updated_timestamp = last_updated_timestamp
        # UserId
        self.user_id = user_id
        # CurrentStage
        self.current_stage = current_stage
        # Description
        self.description = description
        # Source
        self.source = source
        # RunId
        self.run_id = run_id
        # Status
        self.status = status
        # StatusMessage
        self.status_message = status_message
        # Tags
        self.tags = tags
        # RunLink
        self.run_link = run_link

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        if self.creation_timestamp is not None:
            result['creation_timestamp'] = self.creation_timestamp
        if self.last_updated_timestamp is not None:
            result['last_updated_timestamp'] = self.last_updated_timestamp
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.current_stage is not None:
            result['current_stage'] = self.current_stage
        if self.description is not None:
            result['description'] = self.description
        if self.source is not None:
            result['source'] = self.source
        if self.run_id is not None:
            result['run_id'] = self.run_id
        if self.status is not None:
            result['status'] = self.status
        if self.status_message is not None:
            result['status_message'] = self.status_message
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.run_link is not None:
            result['run_link'] = self.run_link
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('creation_timestamp') is not None:
            self.creation_timestamp = m.get('creation_timestamp')
        if m.get('last_updated_timestamp') is not None:
            self.last_updated_timestamp = m.get('last_updated_timestamp')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('current_stage') is not None:
            self.current_stage = m.get('current_stage')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('status_message') is not None:
            self.status_message = m.get('status_message')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ModelVersionTag()
                self.tags.append(temp_model.from_map(k))
        if m.get('run_link') is not None:
            self.run_link = m.get('run_link')
        return self


class RegisteredModel(TeaModel):
    def __init__(
        self,
        name: str = None,
        creation_timestamp: int = None,
        last_updated_timestamp: int = None,
        user_id: str = None,
        description: str = None,
        latest_versions: List[ModelVersion] = None,
        tags: List[RegisteredModelTag] = None,
    ):
        # Name
        self.name = name
        # CreationTimestamp
        self.creation_timestamp = creation_timestamp
        # LastUpdatedTimestamp
        self.last_updated_timestamp = last_updated_timestamp
        # UserId
        self.user_id = user_id
        # Description
        self.description = description
        # LatestVersions
        self.latest_versions = latest_versions
        # Tags
        self.tags = tags

    def validate(self):
        if self.latest_versions:
            for k in self.latest_versions:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.creation_timestamp is not None:
            result['creation_timestamp'] = self.creation_timestamp
        if self.last_updated_timestamp is not None:
            result['last_updated_timestamp'] = self.last_updated_timestamp
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.description is not None:
            result['description'] = self.description
        result['latest_versions'] = []
        if self.latest_versions is not None:
            for k in self.latest_versions:
                result['latest_versions'].append(k.to_map() if k else None)
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('creation_timestamp') is not None:
            self.creation_timestamp = m.get('creation_timestamp')
        if m.get('last_updated_timestamp') is not None:
            self.last_updated_timestamp = m.get('last_updated_timestamp')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('description') is not None:
            self.description = m.get('description')
        self.latest_versions = []
        if m.get('latest_versions') is not None:
            for k in m.get('latest_versions'):
                temp_model = ModelVersion()
                self.latest_versions.append(temp_model.from_map(k))
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = RegisteredModelTag()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateModelVersionRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        source: str = None,
        run_id: str = None,
        tags: List[ModelVersionTag] = None,
        run_link: str = None,
        description: str = None,
    ):
        self.name = name
        self.source = source
        self.run_id = run_id
        self.tags = tags
        self.run_link = run_link
        self.description = description

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.run_id is not None:
            result['run_id'] = self.run_id
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.run_link is not None:
            result['run_link'] = self.run_link
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ModelVersionTag()
                self.tags.append(temp_model.from_map(k))
        if m.get('run_link') is not None:
            self.run_link = m.get('run_link')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class CreateModelVersionResponseBody(TeaModel):
    def __init__(
        self,
        model_version: ModelVersion = None,
    ):
        self.model_version = model_version

    def validate(self):
        if self.model_version:
            self.model_version.validate()

    def to_map(self):
        result = dict()
        if self.model_version is not None:
            result['model_version'] = self.model_version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('model_version') is not None:
            temp_model = ModelVersion()
            self.model_version = temp_model.from_map(m['model_version'])
        return self


class CreateModelVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateModelVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateModelVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExperimentRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        artifact_location: str = None,
    ):
        self.name = name
        self.artifact_location = artifact_location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.artifact_location is not None:
            result['artifact_location'] = self.artifact_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('artifact_location') is not None:
            self.artifact_location = m.get('artifact_location')
        return self


class CreateExperimentResponseBody(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
    ):
        self.experiment_id = experiment_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.experiment_id is not None:
            result['experiment_id'] = self.experiment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('experiment_id') is not None:
            self.experiment_id = m.get('experiment_id')
        return self


class CreateExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateExperimentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LogModelRequest(TeaModel):
    def __init__(
        self,
        run_id: str = None,
        model_json: str = None,
    ):
        self.run_id = run_id
        self.model_json = model_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.run_id is not None:
            result['run_id'] = self.run_id
        if self.model_json is not None:
            result['model_json'] = self.model_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')
        if m.get('model_json') is not None:
            self.model_json = m.get('model_json')
        return self


class LogModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class SearchModelVersionsRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        max_results: int = None,
        order_by: List[str] = None,
        page_token: str = None,
    ):
        self.filter = filter
        self.max_results = max_results
        self.order_by = order_by
        self.page_token = page_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.max_results is not None:
            result['max_results'] = self.max_results
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.page_token is not None:
            result['page_token'] = self.page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('max_results') is not None:
            self.max_results = m.get('max_results')
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        if m.get('page_token') is not None:
            self.page_token = m.get('page_token')
        return self


class SearchModelVersionsShrinkRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        max_results: int = None,
        order_by_shrink: str = None,
        page_token: str = None,
    ):
        self.filter = filter
        self.max_results = max_results
        self.order_by_shrink = order_by_shrink
        self.page_token = page_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.max_results is not None:
            result['max_results'] = self.max_results
        if self.order_by_shrink is not None:
            result['order_by'] = self.order_by_shrink
        if self.page_token is not None:
            result['page_token'] = self.page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('max_results') is not None:
            self.max_results = m.get('max_results')
        if m.get('order_by') is not None:
            self.order_by_shrink = m.get('order_by')
        if m.get('page_token') is not None:
            self.page_token = m.get('page_token')
        return self


class SearchModelVersionsResponseBody(TeaModel):
    def __init__(
        self,
        model_versions: List[ModelVersion] = None,
        next_page_token: str = None,
    ):
        self.model_versions = model_versions
        self.next_page_token = next_page_token

    def validate(self):
        if self.model_versions:
            for k in self.model_versions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['model_versions'] = []
        if self.model_versions is not None:
            for k in self.model_versions:
                result['model_versions'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['next_page_token'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model_versions = []
        if m.get('model_versions') is not None:
            for k in m.get('model_versions'):
                temp_model = ModelVersion()
                self.model_versions.append(temp_model.from_map(k))
        if m.get('next_page_token') is not None:
            self.next_page_token = m.get('next_page_token')
        return self


class SearchModelVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchModelVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchModelVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchRunsRequest(TeaModel):
    def __init__(
        self,
        experiment_ids: List[str] = None,
        filter: str = None,
        run_view_type: str = None,
        max_results: int = None,
        order_by: List[str] = None,
        page_token: str = None,
    ):
        self.experiment_ids = experiment_ids
        self.filter = filter
        self.run_view_type = run_view_type
        self.max_results = max_results
        self.order_by = order_by
        self.page_token = page_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.experiment_ids is not None:
            result['experiment_ids'] = self.experiment_ids
        if self.filter is not None:
            result['filter'] = self.filter
        if self.run_view_type is not None:
            result['run_view_type'] = self.run_view_type
        if self.max_results is not None:
            result['max_results'] = self.max_results
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.page_token is not None:
            result['page_token'] = self.page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('experiment_ids') is not None:
            self.experiment_ids = m.get('experiment_ids')
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('run_view_type') is not None:
            self.run_view_type = m.get('run_view_type')
        if m.get('max_results') is not None:
            self.max_results = m.get('max_results')
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        if m.get('page_token') is not None:
            self.page_token = m.get('page_token')
        return self


class SearchRunsResponseBody(TeaModel):
    def __init__(
        self,
        runs: List[Run] = None,
        next_page_token: str = None,
    ):
        self.runs = runs
        self.next_page_token = next_page_token

    def validate(self):
        if self.runs:
            for k in self.runs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['runs'] = []
        if self.runs is not None:
            for k in self.runs:
                result['runs'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['next_page_token'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.runs = []
        if m.get('runs') is not None:
            for k in m.get('runs'):
                temp_model = Run()
                self.runs.append(temp_model.from_map(k))
        if m.get('next_page_token') is not None:
            self.next_page_token = m.get('next_page_token')
        return self


class SearchRunsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchRunsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchRunsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExperimentsRequest(TeaModel):
    def __init__(
        self,
        view_type: str = None,
    ):
        # A short description of struct
        self.view_type = view_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.view_type is not None:
            result['ViewType'] = self.view_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ViewType') is not None:
            self.view_type = m.get('ViewType')
        return self


class ListExperimentsResponseBody(TeaModel):
    def __init__(
        self,
        experiments: List[Experiment] = None,
    ):
        self.experiments = experiments

    def validate(self):
        if self.experiments:
            for k in self.experiments:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['experiments'] = []
        if self.experiments is not None:
            for k in self.experiments:
                result['experiments'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.experiments = []
        if m.get('experiments') is not None:
            for k in m.get('experiments'):
                temp_model = Experiment()
                self.experiments.append(temp_model.from_map(k))
        return self


class ListExperimentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListExperimentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListExperimentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetExperimentTagRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        key: str = None,
        value: str = None,
    ):
        self.experiment_id = experiment_id
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.experiment_id is not None:
            result['experiment_id'] = self.experiment_id
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('experiment_id') is not None:
            self.experiment_id = m.get('experiment_id')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class SetExperimentTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class LogParamRequest(TeaModel):
    def __init__(
        self,
        run_id: str = None,
        key: str = None,
        value: str = None,
    ):
        self.run_id = run_id
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.run_id is not None:
            result['run_id'] = self.run_id
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class LogParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetLatestVersionsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        stages: List[str] = None,
    ):
        self.name = name
        self.stages = stages

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.stages is not None:
            result['stages'] = self.stages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('stages') is not None:
            self.stages = m.get('stages')
        return self


class GetLatestVersionsShrinkRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        stages_shrink: str = None,
    ):
        self.name = name
        self.stages_shrink = stages_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.stages_shrink is not None:
            result['stages'] = self.stages_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('stages') is not None:
            self.stages_shrink = m.get('stages')
        return self


class GetLatestVersionsResponseBody(TeaModel):
    def __init__(
        self,
        model_versions: List[ModelVersion] = None,
    ):
        self.model_versions = model_versions

    def validate(self):
        if self.model_versions:
            for k in self.model_versions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['model_versions'] = []
        if self.model_versions is not None:
            for k in self.model_versions:
                result['model_versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model_versions = []
        if m.get('model_versions') is not None:
            for k in m.get('model_versions'):
                temp_model = ModelVersion()
                self.model_versions.append(temp_model.from_map(k))
        return self


class GetLatestVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLatestVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLatestVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransitionModelVersionStageRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
        stage: str = None,
        archive_existing_versions: bool = None,
    ):
        self.name = name
        self.version = version
        self.stage = stage
        self.archive_existing_versions = archive_existing_versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        if self.stage is not None:
            result['stage'] = self.stage
        if self.archive_existing_versions is not None:
            result['archive_existing_versions'] = self.archive_existing_versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('stage') is not None:
            self.stage = m.get('stage')
        if m.get('archive_existing_versions') is not None:
            self.archive_existing_versions = m.get('archive_existing_versions')
        return self


class TransitionModelVersionStageResponseBody(TeaModel):
    def __init__(
        self,
        model_version: ModelVersion = None,
    ):
        self.model_version = model_version

    def validate(self):
        if self.model_version:
            self.model_version.validate()

    def to_map(self):
        result = dict()
        if self.model_version is not None:
            result['model_version'] = self.model_version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('model_version') is not None:
            temp_model = ModelVersion()
            self.model_version = temp_model.from_map(m['model_version'])
        return self


class TransitionModelVersionStageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TransitionModelVersionStageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TransitionModelVersionStageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameRegisteredModelRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        new_name: str = None,
    ):
        self.name = name
        self.new_name = new_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.new_name is not None:
            result['new_name'] = self.new_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('new_name') is not None:
            self.new_name = m.get('new_name')
        return self


class RenameRegisteredModelResponseBody(TeaModel):
    def __init__(
        self,
        registered_model: RegisteredModel = None,
    ):
        self.registered_model = registered_model

    def validate(self):
        if self.registered_model:
            self.registered_model.validate()

    def to_map(self):
        result = dict()
        if self.registered_model is not None:
            result['registered_model'] = self.registered_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('registered_model') is not None:
            temp_model = RegisteredModel()
            self.registered_model = temp_model.from_map(m['registered_model'])
        return self


class RenameRegisteredModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenameRegisteredModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenameRegisteredModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRunRequest(TeaModel):
    def __init__(
        self,
        run_id: str = None,
    ):
        self.run_id = run_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.run_id is not None:
            result['run_id'] = self.run_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')
        return self


class DeleteRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class CreateRunRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
        user_id: str = None,
        start_time: int = None,
        tags: List[RunTag] = None,
    ):
        self.experiment_id = experiment_id
        self.user_id = user_id
        self.start_time = start_time
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.experiment_id is not None:
            result['experiment_id'] = self.experiment_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.start_time is not None:
            result['start_time'] = self.start_time
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('experiment_id') is not None:
            self.experiment_id = m.get('experiment_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = RunTag()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateRunResponseBody(TeaModel):
    def __init__(
        self,
        run: Run = None,
    ):
        self.run = run

    def validate(self):
        if self.run:
            self.run.validate()

    def to_map(self):
        result = dict()
        if self.run is not None:
            result['run'] = self.run.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run') is not None:
            temp_model = Run()
            self.run = temp_model.from_map(m['run'])
        return self


class CreateRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRunResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelVersionTagRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
        key: str = None,
    ):
        self.name = name
        self.version = version
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class DeleteModelVersionTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetRegisteredModelRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetRegisteredModelResponseBody(TeaModel):
    def __init__(
        self,
        registered_model: RegisteredModel = None,
    ):
        self.registered_model = registered_model

    def validate(self):
        if self.registered_model:
            self.registered_model.validate()

    def to_map(self):
        result = dict()
        if self.registered_model is not None:
            result['registered_model'] = self.registered_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('registered_model') is not None:
            temp_model = RegisteredModel()
            self.registered_model = temp_model.from_map(m['registered_model'])
        return self


class GetRegisteredModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRegisteredModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRegisteredModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRunRequest(TeaModel):
    def __init__(
        self,
        run_id: str = None,
    ):
        self.run_id = run_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.run_id is not None:
            result['run_id'] = self.run_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')
        return self


class GetRunResponseBody(TeaModel):
    def __init__(
        self,
        run: Run = None,
    ):
        self.run = run

    def validate(self):
        if self.run:
            self.run.validate()

    def to_map(self):
        result = dict()
        if self.run is not None:
            result['run'] = self.run.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run') is not None:
            temp_model = Run()
            self.run = temp_model.from_map(m['run'])
        return self


class GetRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRunResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMetricHistoryRequest(TeaModel):
    def __init__(
        self,
        run_id: str = None,
        metric_key: str = None,
    ):
        self.run_id = run_id
        self.metric_key = metric_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.run_id is not None:
            result['run_id'] = self.run_id
        if self.metric_key is not None:
            result['metric_key'] = self.metric_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')
        if m.get('metric_key') is not None:
            self.metric_key = m.get('metric_key')
        return self


class GetMetricHistoryResponseBody(TeaModel):
    def __init__(
        self,
        metrics: List[Metric] = None,
    ):
        self.metrics = metrics

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['metrics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('metrics') is not None:
            for k in m.get('metrics'):
                temp_model = Metric()
                self.metrics.append(temp_model.from_map(k))
        return self


class GetMetricHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMetricHistoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMetricHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExperimentRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
    ):
        # A short description of struct
        self.experiment_id = experiment_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.experiment_id is not None:
            result['experiment_id'] = self.experiment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('experiment_id') is not None:
            self.experiment_id = m.get('experiment_id')
        return self


class GetExperimentResponseBody(TeaModel):
    def __init__(
        self,
        experiment: Experiment = None,
    ):
        # experiment
        self.experiment = experiment

    def validate(self):
        if self.experiment:
            self.experiment.validate()

    def to_map(self):
        result = dict()
        if self.experiment is not None:
            result['experiment'] = self.experiment.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('experiment') is not None:
            temp_model = Experiment()
            self.experiment = temp_model.from_map(m['experiment'])
        return self


class GetExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetExperimentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetExperimentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchRegisteredModelsRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        max_results: int = None,
        order_by: List[str] = None,
        page_token: str = None,
    ):
        self.filter = filter
        self.max_results = max_results
        self.order_by = order_by
        self.page_token = page_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.max_results is not None:
            result['max_results'] = self.max_results
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.page_token is not None:
            result['page_token'] = self.page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('max_results') is not None:
            self.max_results = m.get('max_results')
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        if m.get('page_token') is not None:
            self.page_token = m.get('page_token')
        return self


class SearchRegisteredModelsShrinkRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        max_results: int = None,
        order_by_shrink: str = None,
        page_token: str = None,
    ):
        self.filter = filter
        self.max_results = max_results
        self.order_by_shrink = order_by_shrink
        self.page_token = page_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.filter is not None:
            result['filter'] = self.filter
        if self.max_results is not None:
            result['max_results'] = self.max_results
        if self.order_by_shrink is not None:
            result['order_by'] = self.order_by_shrink
        if self.page_token is not None:
            result['page_token'] = self.page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')
        if m.get('max_results') is not None:
            self.max_results = m.get('max_results')
        if m.get('order_by') is not None:
            self.order_by_shrink = m.get('order_by')
        if m.get('page_token') is not None:
            self.page_token = m.get('page_token')
        return self


class SearchRegisteredModelsResponseBody(TeaModel):
    def __init__(
        self,
        registered_models: List[RegisteredModel] = None,
        next_page_token: str = None,
    ):
        self.registered_models = registered_models
        self.next_page_token = next_page_token

    def validate(self):
        if self.registered_models:
            for k in self.registered_models:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['registered_models'] = []
        if self.registered_models is not None:
            for k in self.registered_models:
                result['registered_models'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['next_page_token'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.registered_models = []
        if m.get('registered_models') is not None:
            for k in m.get('registered_models'):
                temp_model = RegisteredModel()
                self.registered_models.append(temp_model.from_map(k))
        if m.get('next_page_token') is not None:
            self.next_page_token = m.get('next_page_token')
        return self


class SearchRegisteredModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchRegisteredModelsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchRegisteredModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRegisteredModelRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
    ):
        self.name = name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateRegisteredModelResponseBody(TeaModel):
    def __init__(
        self,
        registered_model: RegisteredModel = None,
    ):
        self.registered_model = registered_model

    def validate(self):
        if self.registered_model:
            self.registered_model.validate()

    def to_map(self):
        result = dict()
        if self.registered_model is not None:
            result['registered_model'] = self.registered_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('registered_model') is not None:
            temp_model = RegisteredModel()
            self.registered_model = temp_model.from_map(m['registered_model'])
        return self


class UpdateRegisteredModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRegisteredModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateRegisteredModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelVersionRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DeleteModelVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class SetRegisteredModelTagRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        key: str = None,
        value: str = None,
    ):
        self.name = name
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class SetRegisteredModelTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class SetTagRequest(TeaModel):
    def __init__(
        self,
        run_id: str = None,
        key: str = None,
        value: str = None,
    ):
        self.run_id = run_id
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.run_id is not None:
            result['run_id'] = self.run_id
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class SetTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteTagRequest(TeaModel):
    def __init__(
        self,
        run_id: str = None,
        key: str = None,
    ):
        self.run_id = run_id
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.run_id is not None:
            result['run_id'] = self.run_id
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class DeleteTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ListRegisteredModelsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        page_token: str = None,
    ):
        self.max_results = max_results
        self.page_token = page_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_results is not None:
            result['max_results'] = self.max_results
        if self.page_token is not None:
            result['page_token'] = self.page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('max_results') is not None:
            self.max_results = m.get('max_results')
        if m.get('page_token') is not None:
            self.page_token = m.get('page_token')
        return self


class ListRegisteredModelsResponseBody(TeaModel):
    def __init__(
        self,
        registered_models: List[RegisteredModel] = None,
        next_page_token: str = None,
    ):
        self.registered_models = registered_models
        self.next_page_token = next_page_token

    def validate(self):
        if self.registered_models:
            for k in self.registered_models:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['registered_models'] = []
        if self.registered_models is not None:
            for k in self.registered_models:
                result['registered_models'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['next_page_token'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.registered_models = []
        if m.get('registered_models') is not None:
            for k in m.get('registered_models'):
                temp_model = RegisteredModel()
                self.registered_models.append(temp_model.from_map(k))
        if m.get('next_page_token') is not None:
            self.next_page_token = m.get('next_page_token')
        return self


class ListRegisteredModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRegisteredModelsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRegisteredModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRunRequest(TeaModel):
    def __init__(
        self,
        run_id: str = None,
        status: str = None,
        end_time: int = None,
    ):
        self.run_id = run_id
        self.status = status
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.run_id is not None:
            result['run_id'] = self.run_id
        if self.status is not None:
            result['status'] = self.status
        if self.end_time is not None:
            result['end_time'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        return self


class UpdateRunResponseBody(TeaModel):
    def __init__(
        self,
        run_info: RunInfo = None,
    ):
        self.run_info = run_info

    def validate(self):
        if self.run_info:
            self.run_info.validate()

    def to_map(self):
        result = dict()
        if self.run_info is not None:
            result['run_info'] = self.run_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run_info') is not None:
            temp_model = RunInfo()
            self.run_info = temp_model.from_map(m['run_info'])
        return self


class UpdateRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRunResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreRunRequest(TeaModel):
    def __init__(
        self,
        run_id: str = None,
    ):
        self.run_id = run_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.run_id is not None:
            result['run_id'] = self.run_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')
        return self


class RestoreRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class CreateRegisteredModelRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        tags: List[RegisteredModelTag] = None,
        description: str = None,
    ):
        self.name = name
        self.tags = tags
        self.description = description

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = RegisteredModelTag()
                self.tags.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class CreateRegisteredModelResponseBody(TeaModel):
    def __init__(
        self,
        registered_model: RegisteredModel = None,
    ):
        self.registered_model = registered_model

    def validate(self):
        if self.registered_model:
            self.registered_model.validate()

    def to_map(self):
        result = dict()
        if self.registered_model is not None:
            result['registered_model'] = self.registered_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('registered_model') is not None:
            temp_model = RegisteredModel()
            self.registered_model = temp_model.from_map(m['registered_model'])
        return self


class CreateRegisteredModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRegisteredModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRegisteredModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetModelVersionTagRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
        key: str = None,
        value: str = None,
    ):
        self.name = name
        self.version = version
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class SetModelVersionTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetExperimentByNameRequest(TeaModel):
    def __init__(
        self,
        experiment_name: str = None,
    ):
        # experiment_name
        self.experiment_name = experiment_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.experiment_name is not None:
            result['experiment_name'] = self.experiment_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('experiment_name') is not None:
            self.experiment_name = m.get('experiment_name')
        return self


class GetExperimentByNameResponseBody(TeaModel):
    def __init__(
        self,
        experiment: Experiment = None,
    ):
        # experiment
        self.experiment = experiment

    def validate(self):
        if self.experiment:
            self.experiment.validate()

    def to_map(self):
        result = dict()
        if self.experiment is not None:
            result['experiment'] = self.experiment.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('experiment') is not None:
            temp_model = Experiment()
            self.experiment = temp_model.from_map(m['experiment'])
        return self


class GetExperimentByNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetExperimentByNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetExperimentByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelVersionRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetModelVersionResponseBody(TeaModel):
    def __init__(
        self,
        model_version: ModelVersion = None,
    ):
        self.model_version = model_version

    def validate(self):
        if self.model_version:
            self.model_version.validate()

    def to_map(self):
        result = dict()
        if self.model_version is not None:
            result['model_version'] = self.model_version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('model_version') is not None:
            temp_model = ModelVersion()
            self.model_version = temp_model.from_map(m['model_version'])
        return self


class GetModelVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetModelVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetModelVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreExperimentRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
    ):
        self.experiment_id = experiment_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.experiment_id is not None:
            result['experiment_id'] = self.experiment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('experiment_id') is not None:
            self.experiment_id = m.get('experiment_id')
        return self


class RestoreExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class UpdateExperimentRequest(TeaModel):
    def __init__(
        self,
        new_name: str = None,
        experiment_id: str = None,
    ):
        self.new_name = new_name
        self.experiment_id = experiment_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.new_name is not None:
            result['new_name'] = self.new_name
        if self.experiment_id is not None:
            result['experiment_id'] = self.experiment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('new_name') is not None:
            self.new_name = m.get('new_name')
        if m.get('experiment_id') is not None:
            self.experiment_id = m.get('experiment_id')
        return self


class UpdateExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteRegisteredModelTagRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        key: str = None,
    ):
        self.name = name
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class DeleteRegisteredModelTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteExperimentRequest(TeaModel):
    def __init__(
        self,
        experiment_id: str = None,
    ):
        self.experiment_id = experiment_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.experiment_id is not None:
            result['experiment_id'] = self.experiment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('experiment_id') is not None:
            self.experiment_id = m.get('experiment_id')
        return self


class DeleteExperimentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class GetModelVersionDownloadUriRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetModelVersionDownloadUriResponseBody(TeaModel):
    def __init__(
        self,
        artifact_uri: str = None,
    ):
        self.artifact_uri = artifact_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.artifact_uri is not None:
            result['artifact_uri'] = self.artifact_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifact_uri') is not None:
            self.artifact_uri = m.get('artifact_uri')
        return self


class GetModelVersionDownloadUriResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetModelVersionDownloadUriResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetModelVersionDownloadUriResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LogMetricRequest(TeaModel):
    def __init__(
        self,
        run_id: str = None,
        key: str = None,
        value: float = None,
        timestamp: int = None,
        step: int = None,
    ):
        self.run_id = run_id
        self.key = key
        self.value = value
        self.timestamp = timestamp
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.run_id is not None:
            result['run_id'] = self.run_id
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.step is not None:
            result['step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('step') is not None:
            self.step = m.get('step')
        return self


class LogMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class ListArtifactsRequest(TeaModel):
    def __init__(
        self,
        run_id: str = None,
        path: str = None,
        page_token: str = None,
    ):
        self.run_id = run_id
        self.path = path
        self.page_token = page_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.run_id is not None:
            result['run_id'] = self.run_id
        if self.path is not None:
            result['path'] = self.path
        if self.page_token is not None:
            result['page_token'] = self.page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('page_token') is not None:
            self.page_token = m.get('page_token')
        return self


class ListArtifactsResponseBody(TeaModel):
    def __init__(
        self,
        root_uri: str = None,
        files: List[FileInfo] = None,
        next_page_token: str = None,
    ):
        self.root_uri = root_uri
        self.files = files
        self.next_page_token = next_page_token

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.root_uri is not None:
            result['root_uri'] = self.root_uri
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.next_page_token is not None:
            result['next_page_token'] = self.next_page_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('root_uri') is not None:
            self.root_uri = m.get('root_uri')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = FileInfo()
                self.files.append(temp_model.from_map(k))
        if m.get('next_page_token') is not None:
            self.next_page_token = m.get('next_page_token')
        return self


class ListArtifactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListArtifactsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListArtifactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LogBatchRequest(TeaModel):
    def __init__(
        self,
        run_id: str = None,
        metrics: List[Metric] = None,
        params: List[Param] = None,
        tags: List[RunTag] = None,
    ):
        self.run_id = run_id
        self.metrics = metrics
        self.params = params
        self.tags = tags

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()
        if self.params:
            for k in self.params:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.run_id is not None:
            result['run_id'] = self.run_id
        result['metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['metrics'].append(k.to_map() if k else None)
        result['params'] = []
        if self.params is not None:
            for k in self.params:
                result['params'].append(k.to_map() if k else None)
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')
        self.metrics = []
        if m.get('metrics') is not None:
            for k in m.get('metrics'):
                temp_model = Metric()
                self.metrics.append(temp_model.from_map(k))
        self.params = []
        if m.get('params') is not None:
            for k in m.get('params'):
                temp_model = Param()
                self.params.append(temp_model.from_map(k))
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = RunTag()
                self.tags.append(temp_model.from_map(k))
        return self


class LogBatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class DeleteRegisteredModelRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DeleteRegisteredModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
    ):
        self.headers = headers

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self


class UpdateModelVersionRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
        description: str = None,
    ):
        self.name = name
        self.version = version
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateModelVersionResponseBody(TeaModel):
    def __init__(
        self,
        model_version: ModelVersion = None,
    ):
        self.model_version = model_version

    def validate(self):
        if self.model_version:
            self.model_version.validate()

    def to_map(self):
        result = dict()
        if self.model_version is not None:
            result['model_version'] = self.model_version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('model_version') is not None:
            temp_model = ModelVersion()
            self.model_version = temp_model.from_map(m['model_version'])
        return self


class UpdateModelVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateModelVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateModelVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


