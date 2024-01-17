#!/usr/bin/env python3
"""
a function task_wait_random that takes an integer max_delay and,
returns a asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for the wait_random coroutine with the given
    max_delay.

    Parameters:
        - max_delay: Maximum delay for wait_random.

    Returns:
        - asyncio.Task object.
    """
    # Create an asyncio.Task for the wait_random coroutine
    task = asyncio.create_task(wait_random(max_delay))
    return task
