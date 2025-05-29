with open('30_file/with.txt', 'w') as f:
    f.write('Hello, World!')
    f.write('This is a test file.')
# 使用with语句打开文件，自动管理资源
with open('30_file/with.txt', 'r') as f:
    content = f.read()
    print(content)  # 输出：Hello, World!