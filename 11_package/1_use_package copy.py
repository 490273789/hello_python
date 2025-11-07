from tools import tools


# 包是用来管理模块的
# 从包中倒入模块：import 包名.模块名 [as 别名]


result = tools.multiply(5, 3)
print(f"5 * 3 = {result}")

result = tools.to_binary(5)
print(f"5 in binary is {result}")

result = tools.to_hexadecimal(5)
print(f"5 in hexadecimal is {result}")
