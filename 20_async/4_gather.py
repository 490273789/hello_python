
import asyncio
import time

async def async_download(url):
    print(f"开始下载 {url}")
    await asyncio.sleep(2)  # 模拟异步网络请求
    print(f"下载完成 {url}")


async def main():
    start = time.time()

    # 这里的 gather 是把多个协程打包，一起扔给 Event Loop
    # 就像你一次性把三张单子扔进厨房
    # return_exceptions=True,将会吧异常作为返回值，而不是抛出异常
    # 如果发生异常：异常的会被取消，其他的正常运行
    await asyncio.gather(
        async_download("百度"), async_download("谷歌"), async_download("必应"), return_exceptions=True
    )

    print(f"异步耗时: {time.time() - start:.2f}秒")


asyncio.run(main())
# 结果：大约 2 秒（因为大家是同时等的！）
