#!/usr/bin/env python3
"""
Module with the measure_time function that measures the total
execution time for wait_n(n, max_delay), and returns
total_time / n.
"""

import time
from typing import List
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure_time function"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
