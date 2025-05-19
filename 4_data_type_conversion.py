# 数据类型之间的转换
# 转int类型
# 字符串转int
str_var = "123"
int_var = int(str_var)
print("int_var:", int_var)  # 123
# 浮点数转int
float_var = 123.456
int_var = int(float_var)
print("int_var:", int_var)  # 123
# 布尔值转int
bool_true, bool_false = True, False
print("int_var:", int(bool_true),int(bool_false))  # 1 0
# int的第二个参数表示进制
# 二进制转int
str_var = "1101"
int_var = int(str_var, 2) # 2 表示，把传入的字符串当做二进制数
print("int_var:", int_var)  # 13

# 转float类型
# 字符串转float
str_var = "123.456"
float_var = float(str_var)
print("float_var:", float_var)  # 123.456
# 整数转float
int_var = 123
float_var = float(int_var)
print("float_var:", float_var)  # 123.0
# 布尔值转float
bool_true, bool_false = True, False
print("float_var:", float(bool_true),float(bool_false))  # 1.0 0.0

# 转布尔类型
# 字符串转布尔值
str_var,str_var1 = "True", ""
bool_var = bool(str_var)
print("bool_var:", bool_var)  # True
bool_var = bool(str_var1)
print("bool_var:", bool_var)  # False
# 整数转布尔值
int_var, int_var1 = 0, 1
bool_var = bool(int_var)
print("bool_var:", bool_var)  # False
bool_var = bool(int_var1)
print("bool_var:", bool_var)  # True
# 浮点数转布尔值
float_var, float_var1 = 0.0, 1.0
bool_var = bool(float_var)
print("bool_var:", bool_var)  # False
bool_var = bool(float_var1)
print("bool_var:", bool_var)  # True

# 转字符串类型
# 整数转字符串
int_var = 123
str_var = str(int_var)
print("str_var:", str_var, type(str_var))  # 123 <class 'str'>
# 浮点数转字符串
float_var = 123.456
str_var = str(float_var)
print("str_var:", str_var, type(str_var))  # 123.456 <class 'str'>
# 布尔值转字符串
bool_var = True
str_var = str(bool_var)
print("str_var:", str_var, type(str_var))  # True <class 'str'>