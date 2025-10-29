# 反转数字，输入123， 输出321；输入-456，输出-654


def reverse_number(number: int) -> int:
    if number < 0:
        number_str = str(-number)
        reverse_str = number_str[::-1]
        return -int(reverse_str)
    else:
        return str(number)[::-1]


print("123:", reverse_number(123))
print("-456:", reverse_number(-456))
