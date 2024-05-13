import time
from loguru import logger

from app import utils
from app import config as cfg

# import snoop

def main() -> None:
    utils.check_storage()

    for i in range(cfg.NUMBER_OF_FILES):
        logger.info(f'Started run {i+1} out of {cfg.NUMBER_OF_FILES}.')

        records = utils.generate_records(cfg.NUMBER_OF_RECORDS)
        utils.upload_data_as_parquet_file(records)

        time.sleep(cfg.FREQUENCY)

        logger.info(f'Finished run {i+1} out of {cfg.NUMBER_OF_FILES}.')

if __name__ == "__main__":
    main()
