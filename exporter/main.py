import io
import json
import random
from datetime import datetime

import jsonlines
from faker import Faker
from loguru import logger

import exporter.config as cfg

# import snoop


def _get_schema() -> dict:
    logger.info("Started to load schema.")

    try:
        with open("exporter/schema.json", mode="r", encoding="utf-8") as json_file:
            dict_file = json.load(json_file)
    except OSError as err:
        logger.error(f"Failed to load schema. Error: {err}.")
        raise

    logger.info("Succeeded to load schema.")
    return dict_file


def _is_record_and_schema_aligned(record: dict, schema: dict) -> bool:
    record_keys = [key for key in record.keys()]
    schema_keys = [key for key in schema.keys()]

    return record_keys == schema_keys


def _generate_record(index: int, schema: dict) -> dict:
    logger.info("Started to generate record.")

    faker = Faker(locale=["en_GB"])
    faker.seed_instance(index)
    record = dict()

    record["name"] = {"first": faker.first_name(), "last": faker.last_name()}
    record["address"] = {"city": faker.city()}
    record["sale"] = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": random.choice(range(0, cfg.MAXIMUM_OF_SALE_AMOUNT, 100)),
    }

    if not _is_record_and_schema_aligned(record, schema):
        raise AttributeError("Schema is not aligned with record fields.")

    logger.info("Succeeded to generate record.")
    return record


def _export_records(records: list) -> None:
    logger.info("Started to export records.")

    file = _convert_records_to_jsonlines_file(records)

    logger.info("Succeeded to export records.")


def _convert_records_to_jsonlines_file(records: list) -> io.BytesIO:
    file = io.BytesIO()
    with jsonlines.Writer(file) as writer:
        writer.write_all(records)

    # for testing only
    # with open("exporter/export.jsonl", mode='wb') as f:
    #     f.write(file.getbuffer())

    file.close()
    return file


def main() -> None:
    schema = _get_schema()
    list_of_records = [
        _generate_record(record, schema) for record in range(cfg.NUMBER_OF_RECORDS)
    ]
    _export_records(list_of_records)


if __name__ == "__main__":
    main()
