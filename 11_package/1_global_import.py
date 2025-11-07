# 包是用来管理模块的
# 全局导入
# 从包中倒入模块：import 包名.模块名 [as 别名]
import tools.math
# import tools.math as mul


result = tools.math.multiply(5, 3)
print(f"5 * 3 = {result}")
