from functools import wraps

from loguru import logger


def log_it(func):
    @wraps(func)
    def wrapper_log_it(*args, **kwargs):
        logger.info(f"Started {func.__name__}.")
        func(*args, **kwargs)
        logger.info(f"Finished {func.__name__}.")
        return func(*args, **kwargs)

    return wrapper_log_it
