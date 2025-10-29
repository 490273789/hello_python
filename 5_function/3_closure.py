# closure
# 1.外部函数嵌套一个内部函数
# 2.内部函数使用了外部函数中的变量
# 3.外部函数返回内部函数


def outer():
    num = 10

    def inner():
        print(num)

    return inner


inn = outer()
inn()
