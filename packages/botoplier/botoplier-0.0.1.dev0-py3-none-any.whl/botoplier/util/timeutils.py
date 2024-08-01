import time
from typing import Callable

LoggerFn = Callable[[str], None]

def time_usage(logger_fn: LoggerFn) -> str:
    """A decorator that will log timing of the decorated function every time it's called."""

    def decorator(func):
        def timeusage_wrapper(*args, **kwargs):
            beg_ts = time.time()
            retval = func(*args, **kwargs)
            end_ts = time.time()
            # XXX correct for stack depth similar to loguru's .opt(depth=1)
            logger_fn(f"{func.__name__}(...) took %.03fs" % (end_ts - beg_ts))
            return retval

        return timeusage_wrapper

    return decorator
