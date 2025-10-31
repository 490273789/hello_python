import os

# open方法的第二个参数
# r 只读模式，文件必须存在，不然会报错，默认的模式
# w 写入模式，如果文件存在则覆盖，不存在则创建
# a（append） 追加模式，如果文件存在则在末尾添加内容，不存在则创建
# x：创建新文件并写入，如果文件存在会报错
# b 以二进制打开，一般用于非文本文件，如图片
# t 以文本方式打开，默认此方式
# + 能读能写
# a+ 追加读写模式，可以在文件末尾添加内容，同时可以读取文件
# r+ 读写模式，可以同时读写文件，如果文件不存在则报错
# w+ 读写模式，如果文件存在则覆盖，不存在则创建

# 第三个参数encoding
# encoding="utf-8" 指定文件编码格式，默认为系统编码
# encoding="gbk" 指定文件编码格式为GBK
# encoding="utf-8-sig" 指定文件编码格式为UTF-8带BOM
# encoding="utf-16" 指定文件编码格式为UTF-16
# encoding="utf-32" 指定文件编码格式为UTF-32
# encoding="ascii" 指定文件编码格式为ASCII

path = os.getcwd()  # 获取当前工作目录
print("当前工作目录:", path)
# 打开文件
file = open(path + "/6_file/1_test.txt", "r")

# 文件操作是一个管道，如果第一个read读取完了，后面的方法就读取不到了
# 读取文件 read([size]) 不屑参数默认读取所有，size 读取字节的大小
# content = file.read()
# print(""file.read:", content)
content1 = file.read(1)
content3 = file.read(3)
print(f"content1: {content1}")
print(f"content3: {content3}")

# content_line = file.readline()  # 读取一行
# print(f"读取一行：{content_line.strip()}")  # 去除末尾的换行符

# content_lines = file.readlines()  # 读取所有行
# print("读取的所有行:")
# for line in content_lines:
#     print(line.strip())  # 去除每行末尾的换行符

# 关闭文件
file.close()
