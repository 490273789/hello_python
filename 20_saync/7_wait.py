# 可以用于等待多个task或Future对象
# 可以指定在什么情况下才会返回，默认是ALL_COMPLETED，return_when = asyncio.ALL_COMPLETED
# 注意，这个函数不会触发TimeoutError，而是将执行完的和超时的通过元组的形式返回

import asyncio


async def greet(name, s):
    await asyncio.sleep(s)
    return name


# 运行task或者Future对象，不能是写成
# 如果没有指定timeout，永远不会过时
# return_when 除了默认的ALL_coMPLETED 外，还有以下可选值:ALL_COMPLETED:等所有任务都执行完成后再返回。
# FIRST_EXCEPTION:有任何任务发生异常后就立即返回，即使没有超时也会返回。
# FIRST_COMPLETED:第一个任务执行完后就立即返回。
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
