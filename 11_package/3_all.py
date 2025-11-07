# 局部导入：from import *
# 当我们使用 from import*时，Python并不会查找并导入包的所有子模块，因为这将花费很长的时间，并且可能会产生我们不想要的副作用。
# 唯一的解决办法是提供包的显式索引。如果包的 _init_py 中定义了__all__，运行from import *时，它就是被导入的模块名列表。
# 格式：from 包 import *
# from tools import *

# print(f"random_string_list(): {random.random_string_list(10)}")
# print(f"random_string_list(): {random.to_binary(10)}") 报错
