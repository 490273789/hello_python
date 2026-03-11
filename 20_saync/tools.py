import asyncio
import time
from functools import wraps


def async_timed(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        print(f"[{func.__name__}] 开始执行...")
        start = time.perf_counter()
        try:
            return await func(*args, **kwargs)
        finally:
            end = time.perf_counter()
            print(f"[{func.__name__}] 执行耗时: {end - start:.4f} 秒")

    return wrapper


async def greet(name, s):
    await asyncio.sleep(s)
    print(f"greet: {name} {s}")
    return name
