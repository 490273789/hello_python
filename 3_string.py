
# 字符串
print("---------string---------")
str_var = "Hello, World!"
# 单引号、双引号、三引号、str()都可以
str_var1 = 'Hello, World!'
str_var2 = """Hello, World!"""
# 三引号可以换行
str_var3 = '''Hello, 
World!'''
# 字符串拼接
str_var4 = str_var + str_var1
# 字符串乘法
str_var5 = str_var * 3
print("str_var5:",str_var5)  # Hello, World!Hello, World!Hello, World!
# 字符串格式化
str_var6 = "Hello, %s" % "World"
str_var7 = "Hello, {}".format("World")
print("str_var7:",str_var7)  # Hello, World
# f-string 格式化
str_var8 = f"Hello, {str_var}"
print("str_var8:",str_var8)  # Hello, Hello, World!
# 字符串转义
str_var9 = "Hello, \"World!\""
print("str_var9:",str_var9)  # Hello, "World!"
# 字符串索引,索引从0开始,负数索引从-1开始,从后往前
str_var10 = str_var[0]  # H
print("str_var10:",str_var10)  # H
# 字符串切片，第三个参数表示步长
# str_var[start:end:step]
# 从0开始可以省略0
str_var11 = str_var[0:5]  # Hello
print("str_var11:",str_var11)  # Hello
# 整个字符串
str_var11 = str_var[:]  # Hello, World!
print("str_var11:",str_var11)  # Hello, World!
# 字符串长度，从0开始可以省略0，末尾默认是-1
str_var12 = len(str_var)  # 13
print("str_var12:",str_var12)  # 13
# 字符串查找
str_var13 = str_var.find("World")  # 7
print("str_var13:",str_var13)  # 7
# 字符串替换
str_var14 = str_var.replace("World", "Python")  # Hello, Python!
print("str_var14:",str_var14)  # Hello, Python!
# 字符串分割
str_var15 = str_var.split(",")  # ['Hello', ' World!']
print("str_var15:",str_var15)  # ['Hello', ' World!']

# 字符串反转
str_var16 = str_var[::-1]  # !dlroW ,olleH
print("str_var16:",str_var16)  # !dlroW ,olleH