# 模式匹配 python 3.10以上支持
# age = 20
# := python3.8引入的海象运算符

match age := 20:
    case age if age >= 18:
        print("成年")
    case age if age >= 16:
        print("青少年")
    case age if age >= 12:
        print("儿童")
    case 1:
        print("婴儿")
    case _:
        print("未成年")

# 三目运算符
# 表达式1 if 判断条件 else 表达式二
