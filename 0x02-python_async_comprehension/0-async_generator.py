#!/usr/bin/env python3
"""
Coroutine that yields a random number between 0 and 10
"""
import asyncio
import random


async def async_generator() -> None:
    """
    Coroutine that yields a random number between 0 and 10 after,
    waiting for 1 second asynchronously.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
