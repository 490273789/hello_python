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
