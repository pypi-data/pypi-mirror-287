from mlflow.exceptions import MlflowException
from mlflow.protos.databricks_pb2 import ErrorCode, INTERNAL_ERROR


class PaiMlflowException(MlflowException):
    def __init__(self, data):
        error_code = (
            data["error_code"]
            if "error_code" in data
            else ErrorCode.Name(INTERNAL_ERROR)
        )
        message = "{0}: {1}".format(
            error_code, data["message"] if "message" in data else None
        )
        super().__init__(message, error_code=ErrorCode.Value(error_code))

    @classmethod
    def is_valid(cls, data):
        if isinstance(data, dict):
            return "error_code" in data and "message" in data
        else:
            return False
