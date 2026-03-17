# 十进制转换为其它进制，输入的int，输出为字符串
# 十 -> 二
print(bin(66))
# 十 -> 八
print(oct(66))
# 十 -> 十六
print(hex(66))


# 其他进制转十进制，输入字符串，输出int
# 二 -> 十
print(int("0b1000010", 2))

# 八 -> 十
print(int("0o102", 8))

# 十六 -> 十
print(int("0x42", 16))
