from datetime import datetime
from time import sleep

import app.s3_utils as s3_utils
import app.utils as utils
from app.config import NUMBER_OF_FILES, NUMBER_OF_RECORDS, TIME_INTERVAL

# import snoop


# @log_it
def main() -> None:
    s3_utils.create_storage_if_not_exists()

    schema = utils.get_schema()
    records = utils.generate_records(schema, NUMBER_OF_RECORDS)
    utils.write_records_to_file(records)

    s3_utils.upload_file_to_storage(f"sales_data_{datetime.now():%Y-%m-%d %H:%M:%S}")
    utils.delete_local_file()


if __name__ == "__main__":
    for i in range(NUMBER_OF_FILES):
        main()
        sleep(TIME_INTERVAL)
