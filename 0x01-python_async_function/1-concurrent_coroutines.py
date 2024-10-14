#!/usr/bin/env python3
"""A Python3 module."""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous function that waits for a random delay"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
