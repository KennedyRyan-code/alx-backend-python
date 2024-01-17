#!/usr/bin/env python3
"""
Coroutine that executes async_comprehension four times,
in parallel using asyncio.gather.
"""
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel,
    using asyncio.gather.
    Measures the total runtime and returns it.

    Returns:
        - Total runtime.
    """
    start_time = asyncio.get_event_loop().time()

    # Use asyncio.gather to execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()

    # Calculate and return the total runtime
    total_runtime = end_time - start_time
    return total_runtime
