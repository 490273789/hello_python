# 通过直接或间接继承Exception类来创建自己的异常


class CoolException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise CoolException("帅过头了")
except CoolException as e:
    print("自定义异常：", e)

print(f"{'-' * 10}end{'-' * 10}")
