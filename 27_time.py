# time的使用
import time
# 获取当前时间戳
timestamp = time.time()
print("当前时间戳:", timestamp)
# 获取当前时间元组
time_tuple = time.localtime(timestamp)
print("当前时间元组:", time_tuple)
# 获取当前时间字符串
time_string = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)
print("当前时间字符串:", time_string)