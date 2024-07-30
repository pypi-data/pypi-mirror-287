import functools
import time
import psutil
from .csv_logger import manage_csv

LOG_FORMAT = None


def set_log_format(format):
    global LOG_FORMAT
    LOG_FORMAT = format


def monitor_performance(func):
    """Decorator to monitor both execution time and memory usage."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        metrics = {}
        start_time = time.perf_counter()
        process = psutil.Process()
        mem_before = process.memory_info().rss / 1024**2

        result = func(*args, **kwargs)  # Execute the function

        metrics["execution_time"] = f"{time.perf_counter() - start_time:.4f}"
        metrics["memory_usage"] = (
            f"{process.memory_info().rss / 1024 ** 2 - mem_before:.2f}"
        )

        func_name = func.__qualname__.split(".")[0]
        # change func_name from ThisFormat to this_format
        func_name = "".join(
            ["_" + i.lower() if i.isupper() else i for i in func_name]
        ).lstrip("_")
        manage_csv(func_name, metrics, file_path="execution_metrics.csv")
        return result

    return wrapper
