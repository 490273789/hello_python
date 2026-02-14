# 可以用于等待多个task或Future对象，并且可以指定在什么情况下才会返回，默认是ALL_COMPLETED，
# 注意，这个函数不会触发TimeoutError，而是将执行完的和超市的通过远足的形式返回

import asyncio


async def greet(name, s):
    await asyncio.sleep(s)
    return name


# 运行单个协程或者任务
async def main():
    done_tasks, pending_tasks = await asyncio.wait(
        [
            asyncio.create_task(greet("sss", 2)),
            asyncio.create_task(greet("www", 1)),
            asyncio.create_task(greet("nnn", 3)),
        ],
        timeout=2,
    )

    # 循环已经执行完的任务的返回值
    for task in done_tasks:
        print(task.result())
    # 将剩余的任务执行
    results = await asyncio.gather(*pending_tasks)
    print(f"results: {results}")


if __name__ == "__main__":
    asyncio.run(main())
