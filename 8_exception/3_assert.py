# assert - 用于判断一个表达式，在表达式为False的时候出发异常，常用于程序调试
# 语法：assert 表达式 [,异常描述]


# 等价于
# if not 表达式:
#     raise AssertionError(异常描述)
def add(x, y):
    # if not isinstance(x, int) and isinstance(y, int):
    #     raise AssertionError("参数类型错误")
    assert isinstance(x, int) and isinstance(y, int), "参数类型错误"
    return x + y


add(10, "1")
