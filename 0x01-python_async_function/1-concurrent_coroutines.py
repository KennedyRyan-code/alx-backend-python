#!/usr/bin/env python3
"""
an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
"""


import asyncio
from typing import List


# Import the wait_random coroutine from the previous file
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronously spawns wait_random coroutine n times with specified
    max_delay.

    Parameters:
        - n: Number of times to spawn wait_random.
        - max_delay: Maximum delay for wait_random.

    Returns:
        - List of delays in ascending order.
    """
    delays = []

    # Create a list to hold the tasks
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Use asyncio.gather to run the tasks concurrently
    results = await asyncio.gather(*tasks)

    # Sort the results in ascending order
    delays = sorted(results)

    return (delays)
