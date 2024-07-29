import os

PAI_ACCESS_KEY_ID = os.environ.get("PAI_ACCESS_KEY_ID")
PAI_ACCESS_KEY_SECRET = os.environ.get("PAI_ACCESS_KEY_SECRET")

OSS_ACCESS_KEY_ID = (
    os.environ.get("MLFLOW_OSS_KEY_ID")
    if os.environ.get("MLFLOW_OSS_KEY_ID")
    else PAI_ACCESS_KEY_ID
)
OSS_ACCESS_KEY_SECRET = (
    os.environ.get("MLFLOW_OSS_KEY_SECRET")
    if os.environ.get("MLFLOW_OSS_KEY_SECRET")
    else PAI_ACCESS_KEY_SECRET
)
