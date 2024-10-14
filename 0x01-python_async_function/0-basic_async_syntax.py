#!/usr/bin/env python3
""" basics of async module"""

import random
import asyncio


async def wait_random(max_delay=10):
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay