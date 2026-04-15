# asyncio提供了专门的超时API，用于限制某些任务的最大执行时间。
# 超时API有两个，分别是:asyncio.timeout 以及 asyncio.timeout_at，以下分别进行讲解。

import asyncio

from tools import async_timed, greet


@async_timed
async def main():
    try:
        async with asyncio.timeout(3):
            task1 = asyncio.create_task(greet("w", 2))
            task2 = asyncio.create_task(greet("s", 1))

            result1 = await task1
            print(f"result1: {result1}")
            result2 = await task2
            print(f"result2: {result2}")
    except asyncio.TimeoutError:
        print("超时了")
        tasks = asyncio.all_tasks()
        print(tasks)


if __name__ == "__main__":
    asyncio.run(main())
