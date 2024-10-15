#!/usr/bin/env python3
"""A Python3 module."""
import asyncio
from typing import List
from 0_basic_async_syntax import wait_random  # Correct import statement


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous function that returns a sorted ist of delays."""
    wait_times = await asyncio.gather(
        *[wait_random(max_delay) for _ in range(n)]
    )
    return sorted(wait_times)
