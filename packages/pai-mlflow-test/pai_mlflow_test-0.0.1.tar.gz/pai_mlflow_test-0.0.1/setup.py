import re
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

version = ""
with open("pai_mlflow/__init__.py", "r") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

if not version:
    raise RuntimeError("Cannot find version information")

setup(
    name="pai-mlflow-test",
    version=version,
    description="Alibaba Cloud PAI MLflow Plugin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://code.alibaba-inc.com/PAI/pai-mlflow-plugin",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "mlflow",
        "oss2",
        "alibabacloud_tea_util>=0.3.3, <1.0.0",
        "alibabacloud_tea_openapi>=0.2.4, <1.0.0",
        "alibabacloud_openapi_util>=0.1.4, <1.0.0",
        "alibabacloud_endpoint_util>=0.0.3, <1.0.0",
    ],
    entry_points={
        # "mlflow.tracking_store": "pai=pai_mlflow.store:get_pai_tracking_store",
        "mlflow.model_registry_store": "pai=pai_mlflow.store:get_pai_model_registry_store",
        "mlflow.artifact_repository": "oss=pai_mlflow.store:get_oss_artifact_repository",
        "mlflow.run_context_provider": "unused=pai_mlflow.store:get_paiflow_run_context",
        "mlflow.tracking_store": "pai-tracking-plugin=pai_mlflow.store.tracking.pai_rest_store:PluginPAIRestStore",
    },
    license="Apache License 2.0",
)
