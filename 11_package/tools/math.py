# 实现一个乘法函数
def multiply(a, b):
    return a * b


# 实现一个转二进制函数
def to_binary(n):
    if n < 0:
        raise ValueError("Negative numbers are not supported")
    return bin(n)[2:]  # 去掉 '0b' 前缀


# 实现一个转十六进制函数
def to_hexadecimal(n):
    if n < 0:
        raise ValueError("Negative numbers are not supported")
    return hex(n)[2:]  # 去掉 '0x' 前缀
