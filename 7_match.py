# 模式匹配 python 3.10以上支持
age = 20

match age:
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