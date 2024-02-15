# py-microservice-app
py-microservice-app

# Project plan
Diagrams
Localstack -> IAM, SecretsManager, S3, SQS, Lambda, DynamoDB, CloudWatch,
PostgreSQL
Terraform
Metabase

# Set up environment
py -m pip install pip --upgrade
py -m pip install virtualenv
py -m virtualenv .venv --python=python3.xx -v
.venv/Scripts/Activate
py -m pip install -r -requirements.txt

# Run Ruff
ruff check . --fix -v
ruff format . -v

# Run Pyright
pyright --verbose

# Run Pytest
pytest -vv

# Run snoop
import snoop
Add @snoop decorator

# Run loguru
from loguru import logger
Add logger.info('')


