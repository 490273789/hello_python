import asyncio

# import time

# 假设这里有一个 sync_get 函数模拟 requests.get
# def sync_download(url):
#     print(f"开始下载 {url}")
#     time.sleep(2)  # 模拟网络延迟
#     print(f"下载完成 {url}")


# start = time.time()
# sync_download("百度")
# sync_download("谷歌")
# sync_download("必应")
# print(f"同步耗时: {time.time() - start:.2f}秒")
# 结果：大约 6 秒（2+2+2）

# import time


async def async_task(name, delay):
    print(f"{name} 开始点餐...")
    # await 是关键！
    # 意思是：我要睡一会儿（模拟网络请求），大管家你去调度别的人吧
    await asyncio.sleep(delay)
    print(f"{name} 的菜好了！")


async def main():
    print("餐厅开始营业")

    # 创建两个任务
    task1 = asyncio.create_task(async_task("客人A", 2))
    task2 = asyncio.create_task(async_task("客人B", 3))

    print("服务员接单完毕，去厨房了...")

    # 等待两个任务都完成
    await task1
    print("await1")
    await task2
    print("await2")
    print("餐厅打烊")


asyncio.run(main())


# async def async_download(url):
#     print(f"开始下载 {url}")
#     await asyncio.sleep(2)  # 模拟异步网络请求
#     print(f"下载完成 {url}")


# async def main():
#     start = time.time()

#     # 这里的 gather 是把多个协程打包，一起扔给 Event Loop
#     # 就像你一次性把三张单子扔进厨房
#     await asyncio.gather(
#         async_download("百度"), async_download("谷歌"), async_download("必应")
#     )

#     print(f"异步耗时: {time.time() - start:.2f}秒")


# asyncio.run(main())
# # 结果：大约 2 秒（因为大家是同时等的！）
