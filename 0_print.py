# print 函数 - print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# sep: 分隔符，默认是空格
# end: 结束符，默认是换行符 \n
# file: 输出到文件，默认是 sys.stdout
# flush: 是否强制刷新输出缓冲区，默认是 False
# print 函数的作用是将指定的对象输出到控制台或文件中

# 打印数字
print(1993)

# 打印字符串
print("Hello Nathan")

# 打印变量
year = 1993
print(year)

print("Hello", "Nathan", year, sep="-", end="!\n")

month = 10
day = 1
week = "星期一"
weather = "晴"
temp = 24.3

# %d: 整数
# %s: 字符串
# %f: 浮点数
# %.2f: 浮点数，保留两位小数
# %%: 输出百分号
print("今天是%d年 %02d月 %02d日 %s 天气%s 气温%.2f度" % (year, month, day, week, weather, temp))
print("今天是{}年{}月{}日{} 天气{} 气温{}度".format(year, month, day, week, weather, temp))
print(f"今天是{year}年{month}月{day}日{week}，天气{weather}，气温{temp}度")

