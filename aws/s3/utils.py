import boto3
import io

endpoint_url = "http://localhost.localstack.cloud:4566"
s3_client = boto3.client(service_name="s3", endpoint_url=endpoint_url, region_name='eu-west-1')
s3_resource = boto3.resource(service_name="s3", endpoint_url=endpoint_url, region_name='eu-west-1')

def upload_file(file, key: str, bucket_name: str) -> None:
        s3_client.put_object(Bucket=bucket_name, Key=key, Body=file)

def create_bucket(bucket_name: str):
    s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})

create_bucket('torbilote')