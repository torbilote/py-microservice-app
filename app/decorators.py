import functools
import time

from loguru import logger


def time_it(func):
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
