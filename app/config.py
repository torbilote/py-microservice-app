import os
# S3
S3_BUCKET_NAME= os.getenv('AWS_ENDPOINT_URL', "app-staging")
AWS_REGION_NAME = os.getenv('AWS_ENDPOINT_URL', "eu-west-1")
AWS_ENDPOINT_URL = os.getenv('AWS_ENDPOINT_URL', "http://localhost:4566")
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', "test")
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', "test")

# Exporter
NUMBER_OF_RECORDS = 100
NUMBER_OF_FILES = 10
TIME_INTERVAL = 5
FILE_PATH = "app/export.jsonl"
