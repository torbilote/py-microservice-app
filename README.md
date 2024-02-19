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

# Set up aws cli localy and localstack in Docker
aws configure

~/.aws/config
[profile localstack]
region=eu-west-1
output=json
endpoint_url = http://localhost:4566

~/.aws/credentials
[localstack]
aws_access_key_id=test
aws_secret_access_key=test

Run localstack container

aws s3 mb s3:// --profile localstack
aws s3 ls --profile localstack


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


