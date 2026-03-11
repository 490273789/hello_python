import asyncio


# 协程
async def async_task(name, delay):
    print(f"{name} 开始点餐...")
    # await 是关键！
    # 意思是：我要睡一会儿（模拟网络请求），大管家你去调度别的人吧
    await asyncio.sleep(delay)
    print(f"{name} 的菜好了！")


async def main():
    print("餐厅开始营业")

    # 创建两个任务
    task1 = asyncio.create_task(async_task("客人A", 4))
    task2 = asyncio.create_task(async_task("客人B", 3))

    print("服务员接单完毕，去厨房了...")

    # 等待两个任务都完成
    await task1
    await task2
    print("餐厅打烊")


if __name__ == "__main__":
    # main()： 创建一个协程，并不是直接运行main函数
    asyncio.run(main())  # 如果没有时间循环会创建一个时间循环，如果有则放入事件循环

# 事件循环
# 有一个协程队列，存储所有需要执行的协程
# queue = [cor1, cor2,...]
# while True:
#     cor = queue.pop()
#     result = await cor
