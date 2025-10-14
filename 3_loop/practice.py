# 打印进度条
import time

num = 0
while num < 100:
    print("=", end="")
    num += 1
    time.sleep(0.5)
