import boto3
from botocore.client import ClientError
from loguru import logger

from exporter.config import AWS_ENDPOINT_URL, AWS_REGION_NAME, FILE_PATH, S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

s3_client = boto3.client(
    service_name="s3",
    endpoint_url=AWS_ENDPOINT_URL,
    region_name=AWS_REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)
s3_resource = boto3.resource(
    service_name="s3",
    endpoint_url=AWS_ENDPOINT_URL,
    region_name=AWS_REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


def create_storage_if_not_exists() -> None:
    logger.info("Started.")

    try:
        s3_client.head_bucket(Bucket=S3_BUCKET_NAME)
    except ClientError:
        s3_client.create_bucket(
            Bucket=S3_BUCKET_NAME,
            CreateBucketConfiguration={"LocationConstraint": AWS_REGION_NAME},
        )

    logger.info("Finished.")


def upload_file_to_storage(file_name: str) -> None:
    logger.info("Started.")

    s3_client.upload_file(Bucket=S3_BUCKET_NAME, Key=file_name, Filename=FILE_PATH)

    logger.info("Finished.")
