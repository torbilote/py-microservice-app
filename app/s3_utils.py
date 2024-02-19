import boto3
from botocore.client import ClientError

from app.config import AWS_ENDPOINT_URL, AWS_REGION_NAME, S3_BUCKET_NAME

s3_client = boto3.client(
    service_name="s3", endpoint_url=AWS_ENDPOINT_URL, region_name=AWS_REGION_NAME
)
s3_resource = boto3.resource(
    service_name="s3", endpoint_url=AWS_ENDPOINT_URL, region_name=AWS_REGION_NAME
)


def create_storage_if_not_exists() -> None:
    try:
        s3_client.head_bucket(Bucket=S3_BUCKET_NAME)
    except ClientError:
        s3_client.create_bucket(
            Bucket=S3_BUCKET_NAME,
            CreateBucketConfiguration={"LocationConstraint": AWS_REGION_NAME},
        )


def upload_file_to_storage(file_name: str) -> None:
    s3_client.upload_file(
        Bucket=S3_BUCKET_NAME, Key=file_name, Filename="app/export.jsonl"
    )
