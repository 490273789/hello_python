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
    num1 = 20 # 会创建一个和全局num1同名的局部变量，不会改变全局变量
    print(num1)
f()  # 20

print(num1)  # 10

num1 = 10

def f():
    global num1 # 声明 num1 为全局变量，如果是可变的数据类型，改变它的值会改变全局变量，不需要声明global
    num1 = 20 # 会改变全局变量 num1
    print(num1)
f()  # 20

print(num1)  # 20