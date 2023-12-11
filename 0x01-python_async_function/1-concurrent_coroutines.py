#!/usr/bin/env python3
"""
Asynchronous routine wait_n that takes in 2 int arguments (in
this order): n and max_delay. It will spawn wait_random n
times with the specified max_delay.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine"""
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)


if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
