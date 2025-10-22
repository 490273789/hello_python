# with关键字
"""
python中with语句用于异常处理，封装了tyr...except...finally编码范式，
提供了一种简洁的方式来确保资源的正确获取和释放，同时处理可能发生的异常，提高了易用性。
简化了文件流等公共资源的管理。

语法
with expression as variable:
    代码块

expression： 通常是一个对象或函数调用，改对象需要一个上下文管理器，即实现了__enter__和__exit__方法
variable： 是可选的，用于存储expression的__enter__方法的返回值

工作原理
使用with关键字系统会自动调用f.close() 方法，with的作用等校于try finally语句
当执行with语句时，会调用expression对象的__enter__方法。
__enter__方法的返回值可以被存储在variable中，以供with代码块中使用。
然后执行with语句内部的代码块
无论代码块中是否发生异常，都会调用expression对象中的__exit__方法，
以确保资源的释放或清理工作，这类似于try finally中的finally子句

"""


# IO中的两个方法实现
class IOBase:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()  # 关闭文件（刷新缓冲并释放底层文件描述符）
        # 不返回 True，因此不会屏蔽异常
