#!/usr/bin/env python3
"""
Contains an async function
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    done = []
    for task in asyncio.as_completed(tasks):
        done.append(await task)

    return done
