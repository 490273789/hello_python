import os
# 打开文件
file_path = os.path.join(os.getcwd(), '30_file/example.txt')
file = open(file_path, 'w', encoding='utf-8')  # 使用写入模式打开文件，指定编码为UTF-8

# 写入文件
file.write("Hello, World!\n")
file.write("This is a test file.")

# 关闭文件
file.close()