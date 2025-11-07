# 格式： from 模块名 import 成员名 [as 别名],成员名 [as 别名],成员名 [as 别名]
from tools import add, subtract as sub
# 导入这个模块的所有变量，不包含下划线开头的变量
# from tools import *

result = add(5, 3)
print(f"5 + 3 = {result}")

result = sub(5, 3)
print(f"5 - 3 = {result}")
