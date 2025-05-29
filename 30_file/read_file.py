import os

path = os.getcwd()  # 获取当前工作目录
print("当前工作目录:", path)
# 打开文件
file = open(path + "/30_file/test.txt", "r")

# 读取文件
content = file.read()
print(content)
content_line = file.readline()  # 读取一行
print("读取的一行:")
print(content_line.strip())  # 去除末尾的换行符
content_lines = file.readlines()  # 读取所有行
print("读取的所有行:")
for line in content_lines:
    print(line.strip())  # 去除每行末尾的换行符

# 关闭文件
file.close()

# open方法的第二个参数
# r 只读模式，文件必须存在，不然会报错
# w 写入模式，如果文件存在则覆盖，不存在则创建
# a（append） 追加模式，如果文件存在则在末尾添加内容，不存在则创建
# b 二进制模式
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