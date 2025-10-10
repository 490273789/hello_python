import math
from decimal import Decimal

# 命名规则：数字、字母、下划线，不能以数字开头
# 变量需要先定义
x = 5
y = 10
z = x + y

# 定义多个变量，值不同
a, b, c = 1, 2, 3

# 定义多个变量，值相同
a = b = c = 1

# python 没有专用的常量符号，一般用大写表示常量
PI = 3.14

# 数值类型 - 整数、浮点数、复数、布尔

# 可变和不可变类型 mutable and immutable
# 可变类型：list dict set
# 不可变类型：int float str tuple bool

type1 = 1
type2 = True
# 查看变量的数据类型，type不会认为子类是一种父类类型
print(type(type1))  # <class 'int'>
print(type(type2))  # <class 'bool'>

# 查看变量的数据类型，会认为子类是一种父类类型
print(isinstance(type1, int))  # True
print(isinstance(type2, bool))  # True
print(isinstance(type2, int))  # True

# 变量互换
num1 = 1
num2 = 2
num1, num2 = num2, num1
print("num1:", num1)
print("num2:", num2)

# 整形
print("---------int---------")
int_var = 10
# python中的小整数缓存机制
# [-5,256]之间的整数是缓存的，相同数字它们的内存地址是一样的
int_var1 = 5
int_var2 = 5
int_var3 = 256
print("int_var1:", id(int_var1))  # 4387192944
print("int_var2:", id(int_var2))  # 4387192944
print("int_var3:", id(int_var3))  # 4387200976

# 浮点型
print("---------float---------")
float_var = 0.1
float_var1 = 0.2
print(float_var + float_var1)  # 0.30000000000000004
# 解决精度丢失问题
float_var3 = Decimal("0.1")
float_var4 = Decimal("0.2")
print("解决精度丢失：", float_var3 + float_var4)

# 四舍五入
print(round(float_var + float_var1, 2))  # 0.3
float_var2 = 1.0e-3  # 科学计数法
# 向上取整
print(math.ceil(float_var + float_var1))  # 1
# 向下取整
print(math.floor(float_var + float_var1))  # 0

# 布尔型 True 或 False
print("---------bool---------")
# 布尔类型是整数的一个子类型：True == 1 False == 0
# None、0、0.0、""、空容器（[] {} set()）  都是 False
bool_var = True

# 字符串
print("---------string---------")
str_var = "Hello, World!"
print("str_var:", str_var)  # Hello, World!

# 列表 有序列表可以包含任何数据类型
print("---------list---------")
list_var = [1, 2, 3]

# 元组 类似列表但是不可变
print("---------tuple---------")
tuple_var = (1, 2, 3)

# 集合 无序且不重复的数据集合
print("---------set---------")
set_var = {1, 2, 3}

# 字典 键值对的集合
print("---------dict---------")
dict_var = {"a": 1, "b": 2, "c": 3}
