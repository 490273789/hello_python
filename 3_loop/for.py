# for 循环的语句
# in后面需要时可迭代对象

"""
rang([start,] stop [, step])
start: 可选，生成序列的起始值，默认为0
stop: 生成序列的结束值，不包含此值
step: 可选，生成序列的步长，默认1
包前不包后原则
"""

num = 0
for num in range(5):
    print(num)

# for 循环的break语句，结束整个循环，不会执行else
num = 0
for num in range(5):
    if num == 3:
        break
    print(num)
else:
    print("循环结束")

# for 循环的continue语句，结束本次循环，开始下次循环
num = 0
for num in range(5):
    if num == 3:
        continue
    print(num)

# for 循环的pass是循环占位符
num = 0
for num in range(5):
    if num == 3:
        pass
    print(num)

# for 循环的else语句
num = 0
for num in range(5):
    print(num)
else:
    print("循环结束")
