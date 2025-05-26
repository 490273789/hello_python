# 导入某个变量
import sys
sys.path.append('my_module')  # 添加模块所在目录
from tools import add, subtract as sub
# 导入这个模块的所有变量

# from tools import *


result = add(5, 3)
print(f"5 + 3 = {result}")
result = sub(5, 3)
print(f"5 - 3 = {result}")
