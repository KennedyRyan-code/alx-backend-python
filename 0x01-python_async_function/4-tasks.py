#!/usr/bin/env python3
"""
Asynchronously spawns task_wait_random n times with specified max_delay.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronously spawns task_wait_random n times with specified max_delay.

    Parameters:
        - n: Number of times to spawn task_wait_random.
        - max_delay: Maximum delay for task_wait_random.

    Returns:
        - List of delays in ascending order.
    """
    delays = []

    # Create a list to hold the tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Use asyncio.gather to run the tasks concurrently
    results = await asyncio.gather(*tasks)

    # Sort the results in ascending order
    delays = sorted(results)

    return delays
