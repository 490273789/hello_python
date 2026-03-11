import asyncio

from tools import async_timed, greet

# 同步运行
# @async_timed
# async def main():
#     result1 = await greet("w", 2)
#     print(f"result: {result1}")
#     result2 = await greet("s", 1)
#     print(f"result2: {result2}")


# 并发运行
# 1. 需要将任务包装成task对象
@async_timed
async def concurrency():
    task1 = asyncio.create_task(greet("w", 2))
    task2 = asyncio.create_task(greet("s", 1))
    # task1\task2两个任务将会并发执行
    # await是同步代码
    # 最长的执行时间就是两秒，如果不是task需要3秒

    result1 = await task1
    print(f"result: {result1}")

    result2 = await task2
    print(f"result2: {result2}")


if __name__ == "__main__":
    asyncio.run(concurrency())
