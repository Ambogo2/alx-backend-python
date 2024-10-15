#!/usr/bin/env python3
""" multiple coroutines module"""
import asyncio
import heapq
from typing import List

# Import the wait_random function from the '0_basic_async_syntax' module
wait_random = __import__('0_basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    Return a sorted list of all the delays in ascending order.
    """
    # A list to store delays
    delays: List[float] = []
    tasks: List[asyncio.Task] = []

    # Creating and scheduling n coroutines
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    # Gathering results while maintaining a sorted list
    for task in asyncio.as_completed(tasks):
        delay = await task
        heapq.heappush(delays, delay)

    # Return the sorted list
    return list(delays)
