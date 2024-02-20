import os
# S3
S3_BUCKET_NAME = "app-staging"
AWS_REGION_NAME = "eu-west-1"
AWS_ENDPOINT_URL = os.getenv('AWS_ENDPOINT_URL', "http://localhost:4566")

# Exporter
NUMBER_OF_RECORDS = 100
NUMBER_OF_FILES = 10
TIME_INTERVAL = 5
FILE_PATH = "app/export.jsonl"
