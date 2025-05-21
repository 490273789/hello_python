# exception handling
import random

# 常见的错误类型
# 1. SyntaxError: 语法错误
# 2. NameError: 访问一个不存在的变量抛出异常
# 3. TypeError: 类型错误，通常是不同类型之间操作
# 4. IndexError: 索引错误，超出对象索引范围
# 5. KeyError: 键错误，在字典中访问不存在的键
# 6. AttributeError: 属性错误，访问不存在的对象属性
# 7. AssertionError: 断言错误
# 8. OSError: 操作系统产生异常
# 9. ZeroDivisionError: 除零错误，除数为零
# 10. ImportError: 导入模块错误
# 11. ValueError: 值错误，传入函数的参数类型正确但值不正确
# 12. FileNotFoundError: 文件未找到错误
# 13. OverflowError: 溢出错误，数值运算超出范围
# 14. IndentationError: 缩进错误

try:
    num = int(input("请输入一个数字："))
    print("输入的数字是：", num)
    #  随机数
    # result = num / random.randint(0, 10)
    result = random.randint(0, 10) / num
except ValueError:
    print("输入无效，请输入一个数字。")
except ZeroDivisionError as e:
    print("除数不能为零:", e)
except Exception as e:
    print("发生了一个异常：", e)
else:
    print("没有异常发生，执行else代码块。")
    print("结果是：", result)
finally:
    print("finally，无论如何都会执行的代码块。")
