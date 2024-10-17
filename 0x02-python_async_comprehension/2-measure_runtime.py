#!/usr/bin/env python3
"""
Contains an async coroutine
which measure total time
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel
    """
    start = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]

    await asyncio.gather(*tasks)
    end = time.perf_counter()

    return end - start
