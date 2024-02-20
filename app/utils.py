import os
import random
from datetime import datetime

import jsonlines
from faker import Faker
from loguru import logger

from app.config import FILE_PATH


def generate_records(no_of_records: int) -> list[dict]:
    logger.info("Started.")

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

    logger.info("Finished.")
    return records


def write_records_to_file(records: list[dict]) -> None:
    logger.info("Started.")

    with jsonlines.open(FILE_PATH, mode="w") as writer:
        writer.write_all(records)

    logger.info("Finished.")


def delete_local_file() -> None:
    logger.info("Started.")

    os.unlink(FILE_PATH)

    logger.info("Finished.")
