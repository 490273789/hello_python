
import time

# 同步情况下耗时
# 假设这里有一个 sync_get 函数模拟 requests.get
def sync_download(url):
    print(f"开始下载 {url}")
    time.sleep(2)  # 模拟网络延迟
    print(f"下载完成 {url}")


start = time.time()
sync_download("百度")
sync_download("谷歌")
sync_download("必应")
print(f"同步耗时: {time.time() - start:.2f}秒")
# 结果：大约 6 秒（2+2+2）