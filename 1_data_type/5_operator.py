# 算数运算符
# + 加法
# - 减法
# * 乘法
# / 除法
# // 取整除
# % 取余
# ** 幂运算 优先级最高

# 赋值运算符
# = 赋值
# += 加法赋值
# -= 减法赋值
# *= 乘法赋值
# /= 除法赋值
# //= 取整除赋值
# %= 取余赋值
# **= 幂赋值

# 逻辑运算符
# and 逻辑与
# or 逻辑或
# not 逻辑非
# 优先级从高到低依次为：** > * / // % > + - > not > and > or

# 位运算符
# & 按位与
# | 按位或
# ^ 按位异或
# ~ 按位取反 一元运算符
# << 左移
# >> 右移
# 位运算符的优先级低于算数运算符
# 赋值运算符的优先级最低
# 逻辑运算符的优先级低于位运算符

num1 = 17
num2 = 13
print(f"正数与运算：{num1} & {num2}")
print(f"{num1:3} : {num1:08b}")
print(f"{num2:3} : {num2:08b}")
print(f"{num1 & num2:3} : {num1 & num2:08b}")

print(f"正数的或运算: {num1} | {num2}")
print(f"{num1:3} : {num1:08b}")
print(f"{num2:3} : {num2:08b}")
print(f"{num1 | num2:3} : {num1 | num2:08b}")

print(f"正数的异或运算: {num1} ^ {num2}")
print(f"{num1:3} : {num1:08b}")
print(f"{num2:3} : {num2:08b}")
print(f"{num1 ^ num2:3} : {num1 ^ num2:08b}")

print(f"正数的非运算: ~{num1}")
print(f"{num1:3}源码 : {num1:08b}, ")
print(f"{num1:3}取反 : {(1 << 8) - 1:08b}")
print(f"{num1:3}取反 : {(1 << 8) - 1 ^ num1:08b}, 得到补码")
print(f"{~num1:3}源码 : {~num1:08b}，计算出结果的源码")

num3 = -12
print(f"有负数的与计算: {num1} & {num3}")
print(f"{num1:3} : {num1:08b}")
print(f"{num3:3} : {num3:08b}")

print(f"有负数的或计算: {num1} | {num3}")
print(f"{num1:3} : {num1:08b}")
print(f"{num3:3}的源码 : {num3:08b}")
print(f"{num3:3}的反码 : {(1 << 8) - 1 + num3:08b}")  # 补码减1是反码
print(f"{num3:3}的补码 : {(1 << 8) + num3:08b}")  # 时钟加一圈是补码


# 如果是正数的补码，不需要转为源码了，因为正数补码、反码和补码相同
# 如果是负数的补码，需要在转换为源码。


# 成员运算符
# in 成员运算符 在指定的序列中找到值返回True，否则False
# not in 非成员运算符 在指定的序列中没有找到值返回True，否则False

# 身份运算符
# is 身份运算符 判断两个变量是否指向同一个对象
# is not 非身份运算符 判断两个变量是否指向不同的对象
m = 10
n = 10
q = 30
print(f" n is m: {n is m}")

a = [1, 2, 3, 4]
b = a
print(f"a == b: {a == b}")
print(f"a is b: {a is b}")

c = a[:]
print(f"c == b: {c == b}")
print(f"c is b: {c is b}")
# 结论 == 是判断内容相等，is 判断是否指向同一个对象

#  一元运算符
# + 一元加法
# - 一元减法
# ~ 一元按位取反
