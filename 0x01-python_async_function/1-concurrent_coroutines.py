#!/usr/bin/env python3
""" multiple coroutines module"""
import asyncio
import heapq
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    # a list to store delays
    delays = []
    tasks = []

    # Creating and scheduling n coroutines
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    # Gathering results while maintaining a sorted list
    for task in tasks:
        delay = await task
        heapq.heappush(delays, delay)

    # Converting the heap to a sorted list
    return list(delays)
