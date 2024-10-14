#!/usr/bin/env python3
"""A Python3 module."""
import asyncio
from typing import List


wait_random = __import__("0_basic_async_syntax").wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous function that returns sorted list of delays."""
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
