#!/usr/bin/env python3
"""tasks module"""

import importlib.util
from asyncio import Task, create_task

# Dynamically load the '0_basic_async_syntax' module
module_name = '0_basic_async_syntax'
module_path = './0_basic_async_syntax.py'

spec = importlib.util.spec_from_file_location(module_name, module_path)
basic_async_syntax = importlib.util.module_from_spec(spec)
spec.loader.exec_module(basic_async_syntax)

# Access the wait_random function from the dynamically loaded module
wait_random = basic_async_syntax.wait_random


def task_wait_random(max_delay: int) -> Task:
    """Creates and returns an asyncio task for wait_random"""
    task = create_task(wait_random(max_delay))
    return task
