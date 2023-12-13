#!/usr/bin/env python3
"""
Module with an asynchronous generator.
"""

import asyncio
import random


async def async_generator() -> float:
    """
    Coroutine that loops 10 times, waits asynchronously for 1 second,
    then yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
