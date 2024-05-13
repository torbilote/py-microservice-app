import functools
import random
import uuid
from datetime import UTC, datetime
from time import time

import awswrangler as wr
import boto3
import pandas as pd
from faker import Faker
from loguru import logger

from app import config as cfg
from app import schema

s3_client = boto3.client(
    service_name="s3",
    endpoint_url=cfg.AWS_ENDPOINT_URL,
    region_name=cfg.AWS_REGION_NAME,
    aws_access_key_id=cfg.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=cfg.AWS_SECRET_ACCESS_KEY,
)
s3_resource = boto3.resource(
    service_name="s3",
    endpoint_url=cfg.AWS_ENDPOINT_URL,
    region_name=cfg.AWS_REGION_NAME,
    aws_access_key_id=cfg.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=cfg.AWS_SECRET_ACCESS_KEY,
)
s3_session = boto3.Session(
    region_name=cfg.AWS_REGION_NAME,
    aws_access_key_id=cfg.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=cfg.AWS_SECRET_ACCESS_KEY,
)


def generate_records(number_of_records: int) -> list[dict]:
    logger.info("Started.")

    records = list()

    for i in range(number_of_records):
        faker = _get_faker(seed=i)

        name = schema.Name(
            first=faker.first_name(),
            last=faker.last_name(),
        )
        address = schema.Address(
            city=faker.city(),
        )
        sale = schema.Sale(
            date=datetime.now(tz=UTC),
            value=random.choice(range(0, 5000, 100)),
        )
        record = schema.Record(
            name=name,
            address=address,
            sale=sale,
        )
        records.append(record.model_dump())

    logger.info("Finished.")
    return records


def check_storage() -> None:
    logger.info("Started.")

    s3_client.head_bucket(Bucket=cfg.S3_BUCKET_NAME)

    logger.info("Finished.")


def upload_data_as_parquet_file(records: list[dict]) -> None:
    logger.info("Started.")

    if not records:
        logger.error("No records to upload.")
        return

    key = f"{cfg.FILE_NAME_PREFIX}_{uuid.uuid4()}"

    dataframe = pd.DataFrame(data=records)

    wr.s3.to_parquet(
        df=dataframe,
        path=f"s3://{cfg.S3_BUCKET_NAME}/{key}.parquet",
        boto3_session=s3_session,
        index=False,
    )

    logger.info("Finished.")


def _get_faker(seed: int) -> Faker:
    faker = Faker(locale=["en_GB"])
    faker.seed_instance(seed)
    return faker


def _time_it(func):
    @functools.wraps(func)
    def wrapper_time_it(*args, **kwargs):
        logger.info(f"Started {func.__name__}().")

        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        logger.info(f"Finished {func.__name__}() in {run_time:.4f} secs.")
        return value

    return wrapper_time_it
