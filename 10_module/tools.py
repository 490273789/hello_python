# __all__ 设置通过from import * 导入时，哪些内容可以被导出
__all__ = ["add"]

# __name__
# 在 Python 中，__name__是一个特殊的内置变量
# 当一个Python 文件被直接运行时，该文件的_name_属性值为"_main_"
# 当一个 Python 文件作力模块被导入时，_name_属性会被设置为该模块的名称（即文件名，不包含 py 后缀）。
print(f"__ame__: {__name__}")


# 实现一个简单的加法函数
def add(a, b):
    return a + b


# 实现一个简单的减法函数
def subtract(a, b):
    return a - b
