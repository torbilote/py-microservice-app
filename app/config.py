import os

# App
FILE_NAME_PREFIX = os.getenv("FILE_NAME_PREFIX", "data")
NUMBER_OF_FILES = os.getenv("NUMBER_OF_FILES", 50)
NUMBER_OF_RECORDS = os.getenv("NUMBER_OF_RECORDS", 100)
FREQUENCY = os.getenv("FREQUENCY", 5)  # in seconds

# S3
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "staging")
AWS_REGION_NAME = os.getenv("AWS_REGION_NAME", "eu-west-1")
AWS_ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL", "http://localhost:4566")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "test")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "test")
