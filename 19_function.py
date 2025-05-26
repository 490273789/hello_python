from functools import reduce

# 函数
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "除数不能为零"
    return result

# 函数调用
print(divide(10, 2))
print(divide(10, 0))

# 函数不写返回值，默认返回 None
def add(x, y):
    x + y

print(add(10, 20))

# 默认参数
def greet(name, message="你好"):
    print(message, name)

greet("小明")
greet("小红", "欢迎来到我的程序！")

# 可变参数，args 是一个元组
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(add_numbers(1, 2, 3))
print(add_numbers(1, 2, 3, 4, 5))
list_var = [1, 2, 3, 4, 5]
print(add_numbers(*list_var))  # 使用 * 运算符将列表解包为位置参数

# 可变参数和默认参数结合使用
def greet(name, *args, message="你好"):
    print(message, name)
    for arg in args:
        print(arg)
greet("小明", "欢迎来到我的程序！", "今天的天气不错。")

# 可变参数，接收字典
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="小明", age=18, city="北京")
p = {"name": "小明", "age": 18, "city": "北京"}
print_info(**p) # 使用 ** 运算符将字典解包为关键字参数

# 函数注释
def add(x: int, y: int) -> int:
    """
    计算两个数字的和
    :param x: 第一个数字
    :param y: 第二个数字
    :return: 两个数字的和
    """
    return x + y
print(add(10, 20))
# 函数文档
help(add)

# 匿名函数的使用
# add1 = lambda x, y: x + y
list_var = [1, 2, 3, 4, 5]
map_result = map(lambda x: x * 2, list_var)
print(list(map_result))  # [2, 4, 6, 8, 10]

# reduce 函数
reduce_result = reduce(lambda x, y: x + y, list_var)
print(reduce_result)  # 15

def f(x, y):
    print(x, y) 
    return x + y
reduce_result = reduce(f, list_var)

print(reduce_result)  # 15

# filter 函数
filter_result = filter(lambda x: x % 2 == 0, list_var)
print(list(filter_result))  # [2, 4]