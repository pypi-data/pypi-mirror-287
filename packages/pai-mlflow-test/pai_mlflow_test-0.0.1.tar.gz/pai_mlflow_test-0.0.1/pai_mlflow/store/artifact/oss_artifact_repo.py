import os
import posixpath
from urllib import parse

import oss2
from mlflow.entities import FileInfo
from mlflow.exceptions import MissingConfigException
from mlflow.store.artifact.artifact_repo import ArtifactRepository
from mlflow.utils.file_utils import relative_path_to_artifact_path


class OssArtifactRepository(ArtifactRepository):
    def __init__(self, artifact_uri, oss_bucket=None):
        super(OssArtifactRepository, self).__init__(artifact_uri)
        self.bucket, self.oss_endpoint_url, self.dest_path = self._parse_oss_uri(
            artifact_uri
        )
        if oss_bucket is not None:
            self.oss_bucket = oss_bucket
            return
        from pai_mlflow.utils.__global import (
            OSS_ACCESS_KEY_ID,
            OSS_ACCESS_KEY_SECRET,
        )

        self.oss_access_key_id = OSS_ACCESS_KEY_ID
        self.oss_access_key_secret = OSS_ACCESS_KEY_SECRET
        self._validate()
        auth = oss2.Auth(self.oss_access_key_id, self.oss_access_key_secret)
        self.oss_bucket = oss2.Bucket(auth, self.oss_endpoint_url, self.bucket)
        self.is_plugin = True

    @staticmethod
    def _parse_oss_uri(uri):
        """Parse an OSS URI, returning (bucket, path)"""
        parsed = parse.urlparse(uri)
        bucket, endpoint = (
            parsed.netloc.split(".", 1)
            if "." in parsed.netloc
            else (parsed.netloc, None)
        )
        if parsed.scheme != "oss" or endpoint is None:
            raise MissingConfigException(
                "Invalid oss uri, you must specify oss endpoint in uri likes "
                "'oss://your-bucket.oss-{regionId}.aliyuncs.com/path/to/artifact'"
            )
        path = parsed.path
        if path.startswith("/"):
            path = path[1:]
        return bucket, endpoint, path

    def _validate(self):
        if not self.oss_access_key_id:
            raise MissingConfigException(
                "Your oss access key id isn't set. You can specify it in env MLFLOW_OSS_KEY_ID, or just follow "
                "MLFLOW_ALIYUN_KEY_ID which used by tracking store. If both set, the value of MLFLOW_OSS_KEY_ID is "
                "preferred."
            )
        if not self.oss_access_key_secret:
            raise MissingConfigException(
                "Your oss access key secret isn't set. You can specify it in env MLFLOW_OSS_KEY_SECRET, or just follow "
                "MLFLOW_ALIYUN_KEY_SECRET which used by tracking store. If both set, the value of "
                "MLFLOW_OSS_KEY_SECRET is preferred."
            )

    def log_artifact(self, local_file, artifact_path=None):
        dest_path = (
            posixpath.join(self.dest_path, artifact_path)
            if artifact_path
            else posixpath.join(self.dest_path, os.path.basename(local_file))
        )
        self.oss_bucket.put_object_from_file(dest_path, local_file)

    def log_artifacts(self, local_dir, artifact_path=None):
        dest_path = (
            posixpath.join(self.dest_path, artifact_path)
            if artifact_path
            else self.dest_path
        )
        local_dir = os.path.abspath(local_dir)
        for (root, _, filenames) in os.walk(local_dir):
            upload_path = dest_path
            if root != local_dir:
                rel_path = os.path.relpath(root, local_dir)
                rel_path = relative_path_to_artifact_path(rel_path)
                upload_path = posixpath.join(dest_path, rel_path)
            for f in filenames:
                self.oss_bucket.put_object_from_file(
                    posixpath.join(upload_path, f), os.path.join(root, f)
                )

    def list_artifacts(self, path=None):
        dest_path = posixpath.join(self.dest_path, path) if path else self.dest_path
        infos = []
        prefix = dest_path + "/" if dest_path else ""
        for obj in oss2.ObjectIterator(self.oss_bucket, prefix=prefix, delimiter="/"):
            file_path = obj.key
            file_rel_path = posixpath.relpath(path=file_path, start=self.dest_path)
            file_size = obj.size
            infos.append(FileInfo(file_rel_path, obj.is_prefix(), file_size))
        return infos

    def _download_file(self, remote_file_path, local_path):
        oss_full_path = posixpath.join(self.dest_path, remote_file_path)
        self.oss_bucket.get_object_to_file(oss_full_path, local_path)

    def delete_artifacts(self, artifact_path=None):
        def _delete_recursive(oss_bucket, path):
            for obj in oss2.ObjectIterator(oss_bucket, prefix=path, delimiter="/"):
                if not obj.is_prefix():
                    oss_bucket.delete_object(obj.key)
                else:
                    _delete_recursive(oss_bucket, obj.key)

        oss_full_path = (
            posixpath.join(self.dest_path, artifact_path)
            if artifact_path
            else self.dest_path
        )
        _delete_recursive(self.oss_bucket, oss_full_path)
