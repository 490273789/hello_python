
import asyncio


async def task(name, seconds):
    print(f"{name} started")
    await asyncio.sleep(seconds)
    print(f"{name} completed")
    return f"{name} result"


async def main():
    # 方式1：使用 gather 并发执行
    results = await asyncio.gather(task("Task1", 2), task("Task2", 1), task("Task3", 3))
    print(f"Results: {results}")

    # 方式2：使用 create_task
    task1 = asyncio.create_task(task("A", 2))
    task2 = asyncio.create_task(task("B", 1))

    # 可以在这里做其他事情
    await asyncio.sleep(0.5)
    print("Doing other work...")

    # 等待任务完成
    result1 = await task1
    result2 = await task2
    print(f"result1: {result1}")
    print(f"result2: {result2}")


asyncio.run(main())

