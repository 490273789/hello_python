# python 作用域分为4种：
# L（local）局部作用域：只能在当前函数中访问
# E（Enclosing）嵌套作用域，闭包函数：访问父级函数
# G（global）全局作用域：在当前模块中都可以访问
# B（build-in）内建作用域：在所有模块的任意位置都可以访问
# 查找顺序：局部作用域 -> 嵌套作用域 -> 全局作用域 -> 内建作用域

# 全局变量
global_var = "我是全局变量"


def print_global_var():
    print(global_var)


print_global_var()


# 局部变量
def print_local_var():
    local_var = "我是局部变量"
    print(local_var)


num1 = 10


def f():
    # num1 += 1  # 报错，会讲num1当作局部变量处理
    num1 = 20  # 会创建一个和全局num1同名的局部变量，不会改变全局变量
    print(num1)


f()  # 20

print(num1)  # 10

num1 = 10


# global
def f():
    global num1  # 声明 num1 为全局变量，如果是可变的数据类型，改变它的值会改变全局变量，不需要声明global
    num1 = 20  # 会改变全局变量 num1
    print(num1)


f()  # 20

print(num1)  # 20


# nonlocal
def a():
    num2 = 10

    def b():
        nonlocal num2  # 原理同global，作用在嵌套作用域
        num2 = 20
        print(num2)

    print(num2)


a()
