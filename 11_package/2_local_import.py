# 局部导入
# 局部导入包下的模块：from 包名 import 模块 [as 别名]
from tools import math

# 局部导入包下模块的成员：from 包名.模块名 import 成员名 [as 别名]
from tools.random import random_string


result = math.multiply(5, 3)
print(f"5 * 3 = {result}")

result = math.to_binary(5)
print(f"5 in binary is {result}")

result = math.to_hexadecimal(5)
print(f"5 in hexadecimal is {result}")

print(f"random_string(): {random_string()}")
