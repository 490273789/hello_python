# 导入整个模块
# 格式：import 模块名 [as 别名]
import tools


# 导入某个变量
import sys

result = tools.add(5, 3)
print(f"5 + 3 = {result}")

result = tools.subtract(5, 3)
print(f"5 - 3 = {result}")

print(f"模块加载顺序：{sys.path}")
# sys.path.append("my_module")  # 添加模块的查找目录

# 当你将一个模块作为dir0 的参数时，它会返回该模块中定义的名称列表，包括函数、类、变量等
print("dir(tools):", dir(tools))


# 当你将一个对象作为dir 的参数时，它会返回该对象的属性和方法列表。
class CusClass:
    def ___init__(self):
        self.a = 1
        self.b = 3

    def add(self):
        return self.a + self.b


print(f"dir(CusClass): {dir(CusClass)}")

# 当你不传递任何参数调用 dirO时，已会列出当前作用域中定义的名称，包括变量、函数、类等
print(f"dir(): {dir()}")
