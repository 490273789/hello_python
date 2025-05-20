# while 循环
# while 循环的基本语法

num = 0
while num < 5:
    print(num)
    num += 1
# while 循环的else语句
num = 0
while num < 5:
    print(num)
    num += 1
else:
    print("循环结束")
# while 循环的break语句
num = 0
while num < 5:
    if num == 3:
        break
    print(num)
    num += 1
else:
    print("循环结束")
# while 循环的continue语句
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)
# while 循环的pass语句, 占位用的
num = 0
while num < 5:
    num += 1
    if num == 3:
        pass
    print(num)
# for 循环的语句
num = 0
for num in range(5):
    print(num)
# for 循环的break语句
num = 0
for num in range(5):
    if num == 3:
        break
    print(num)
# for 循环的continue语句
num = 0
for num in range(5):
    if num == 3:
        continue
    print(num)
# for 循环的pass语句
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