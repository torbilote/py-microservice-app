import json
import os
import random
from datetime import datetime

import jsonlines
from faker import Faker


def get_schema() -> dict:
    with open("app/schema.json", mode="r", encoding="utf-8") as json_file:
        dict_file = json.load(json_file)
    return dict_file


def _is_record_and_schema_aligned(record: dict, schema: dict) -> bool:
    record_keys = [key for key in record.keys()]
    schema_keys = [key for key in schema.keys()]
    return record_keys == schema_keys


def generate_records(schema: dict, no_of_records: int) -> list[dict]:
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

    if not _is_record_and_schema_aligned(records[0] if records else {}, schema):
        raise AttributeError("Schema is not aligned with record fields.")

    return records


def write_records_to_file(records: list[dict]) -> None:
    with jsonlines.open("app/export.jsonl", mode="w") as writer:
        writer.write_all(records)


def delete_local_file() -> None:
    os.unlink("app/export.jsonl")
