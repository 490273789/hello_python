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

# 生成随机大小写字母
def random_string(length=10):
    import random
    import string
    letters = string.ascii_letters  # 包含所有大小写字母
    return ''.join(random.choice(letters) for _ in range(length))

# 生成一个list，每一项是3到6位的随机字母，list长度为用户传入
def random_string_list(length=5):
    import random
    import string
    letters = string.ascii_letters  # 包含所有大小写字母
    return [''.join(random.choice(letters) for _ in range(random.randint(3, 6))) for _ in range(length)]

# 生成4为验证码，验证码包含数字和字母
def generate_verification_code(length=4):
    import random
    import string
    characters = string.ascii_letters + string.digits  # 包含所有大小写字母和数字
    return ''.join(random.choice(characters) for _ in range(length))