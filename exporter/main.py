import io
import json
import random
from datetime import datetime

import jsonlines
from faker import Faker
from loguru import logger
import os
from time import sleep
from exporter.config import NUMBER_OF_RECORDS, NUMBER_OF_FILES, TIME_INTERVAL
from aws.s3.utils import create_storage_if_not_exists, upload_file_to_storage
# import snoop


def _get_schema() -> dict:
    logger.info("Started to load schema.")

    with open("exporter/schema.json", mode="r", encoding="utf-8") as json_file:
        dict_file = json.load(json_file)

    logger.info("Succeeded to load schema.")
    return dict_file


def _is_record_and_schema_aligned(record: dict, schema: dict) -> bool:
    record_keys = [key for key in record.keys()]
    schema_keys = [key for key in schema.keys()]
    return record_keys == schema_keys


def _generate_records(schema: dict, no_of_records: int) -> list[dict]:
    logger.info("Started to generate records.")

    records = []

    for number in range(no_of_records):
        faker = Faker(locale=["en_GB"])
        faker.seed_instance(number)
        record = dict()

        record["name"] = {
            "first": faker.first_name(),
            "last": faker.last_name(),
        }
        record["address"] = {
            "city": faker.city(),
        }
        record["sale"] = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": random.choice(range(0, 5000, 100)),
        }
        records.append(record)

    if not _is_record_and_schema_aligned(records[0] if records else [], schema):
        raise AttributeError("Schema is not aligned with record fields.")

    logger.info("Succeeded to generate records.")
    return records


def _parse_records_to_file(records: list[dict]) -> None:
    logger.info("Started to parse records to jsonl file.")

    with jsonlines.open('exporter/export.jsonl', mode='w') as writer:
        writer.write_all(records)

    logger.info("Succeeded to parse records to jsonl file.")

def _delete_local_file() -> None:
    os.unlink("exporter/export.jsonl")

if __name__ == "__main__":

    for i in range(NUMBER_OF_FILES):
        logger.info(f"Started to execute {i+1} iteration of the script.")

        create_storage_if_not_exists()

        schema = _get_schema()
        records = _generate_records(schema, NUMBER_OF_RECORDS)
        _parse_records_to_file(records)

        upload_file_to_storage(f"sales_data_{datetime.now():%Y-%m-%d %H:%M:%S}")
        _delete_local_file()

        logger.info(f"Succeeded to execute {i+1} iteration of the script.")
        sleep(TIME_INTERVAL)