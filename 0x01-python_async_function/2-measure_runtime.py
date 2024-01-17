#!/usr/bin/env python3
"""
Measures the total execution time for wait_n(n, max_delay),
and returns total_time / n.
"""
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.

    Parameters:
        - n: Number of times to spawn wait_random.
        - max_delay: Maximum delay for wait_random.

    Returns:
        - Average time per execution.
    """
    start_time = time.time()

    # Use asyncio.run to run the wait_n coroutine
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    # Calculate the total time taken
    total_time = end_time - start_time

    # Calculate and return the average time per execution
    average_time = total_time / n

    return (average_time)
