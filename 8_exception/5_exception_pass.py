# 异常传递


def f1():
    f2()


def f2():
    f3()


def f3():
    return 1 / 0


f1()

# Traceback (most recent call last):
#   File "/Users/ethan/workspace/Python/hello_python/./8_exception/5_exception_pass.py", line 16, in <module>
#     f1()
#   File "/Users/ethan/workspace/Python/hello_python/./8_exception/5_exception_pass.py", line 5, in f1
#     f2()
#   File "/Users/ethan/workspace/Python/hello_python/./8_exception/5_exception_pass.py", line 9, in f2
#     f3()
#   File "/Users/ethan/workspace/Python/hello_python/./8_exception/5_exception_pass.py", line 13, in f3
#     return 1 / 0
#            ~~^~~
# ZeroDivisionError: division by zero
