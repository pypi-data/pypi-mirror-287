# girishcodealchemy/decorators.py

import logging
import time
from functools import wraps

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO)


def log_execution_time(func):
    """
    Decorator to log the execution time of a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper


def log_group(group_name):
    """
    Decorator to create log groups for a function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(f"Entering log group: {group_name}")
            result = func(*args, **kwargs)
            logging.info(f"Exiting log group: {group_name}")
            return result
        return wrapper
    return decorator
