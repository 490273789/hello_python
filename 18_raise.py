# raise 的使用
try:
    x = int(input("请输入一个数字："))
    if x < 0:
        raise ValueError("输入的数字不能为负数。")
except ValueError as e:
    print("发生了一个错误：", e)