import io
import json
import random
from datetime import datetime

import jsonlines
from faker import Faker
from loguru import logger

import exporter.config as exporter_config
# import aws.s3.utils as s3_utils
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
            "amount": random.choice(range(0, exporter_config.MAXIMUM_OF_SALE_AMOUNT, 100)),
        }
        records.append(record)

        if not _is_record_and_schema_aligned(record, schema):
            raise AttributeError("Schema is not aligned with record fields.")

    logger.info("Succeeded to generate records.")
    return records


def _parse_records_to_file(records: list[dict]) -> None:
    logger.info("Started to parse records to jsonl file.")

    # TODO
    file = io.BytesIO()
    with jsonlines.Writer(file) as writer:
        writer.write_all(records)
    with open("exporter/export.jsonl", mode='wb') as f:
        f.write(file.getbuffer())
    file.close()

    logger.info("Succeeded to parse records to jsonl file.")

def _export_file(files) -> None:
    # TODO
    ...

def main() -> None:
    schema = _get_schema()
    records = _generate_records(schema, exporter_config.NUMBER_OF_RECORDS)
    files = _parse_records_to_file(records)
    # _export_file(file)


if __name__ == "__main__":
    main()
