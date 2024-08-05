#!/usr/bin/python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time