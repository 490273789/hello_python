# 内置函数
# abs() 返回数字的绝对值
print(abs(-5))  # 5
# all() 如果可迭代对象中所有元素都为 True（或可迭代对象为空），则返回 True
print(all([True, False, True]))  # False
# any() 如果可迭代对象中至少有一个元素为 True，则返回 True。如果可迭代对象为空，则返回 False
print(any([True, False, True]))  # True
# chr() 返回表示 Unicode 码位为整数 i 的字符的字符串
print(chr(97))  # 'a'
# ord() 返回表示 Unicode 字符的字符串的整数码位
print(ord('a'))  # 97
# dir() 如果没有参数，则返回当前本地作用域中的名称列表。如果有参数，则尝试返回该对象的有效属性列表
print(dir())  # 查看当前作用域的变量
# divmod() 以两个（非复数）数字为参数，并在使用整数除法时返回一对商和余数
print(divmod(10, 3))  # (3, 1)
# enumerate() 返回一个枚举对象。iterable 必须是一个序列、一个迭代器，或者某个其他支持迭代的对象
print(enumerate(['a', 'b', 'c']))  # <enumerate object at 0x7f8c8c0d3f40>
# eval() 将字符串参数解析并作为 Python 表达式求值
print(eval('1 + 2'))  # 3
# filter() 从 iterable 的那些函数返回 True 的元素构造一个迭代器
print(filter(lambda x: x > 0, [-1, 0, 1, 2]))  # <filter object at 0x7f8c8c0d3f40>
# float() 返回从数字或字符串 x 构造的浮点数
print(float('3.14'))  # 3.14
# format() 将值转换为“格式化”的表示形式，由 format_spec 控制
print(format(123456789, ',d'))  # '123,456,789'
# hash() 返回对象的哈希值（如果它有的话）
print(hash('hello'))  # 99162322
# hex() 将整数转换为以“0x”为前缀的小写十六进制字符串
print(hex(255))  # '0xff'
# id() 返回对象的“标识”。这是一个整数，保证在该对象的生命周期内是唯一且恒定的
print(id('hello'))  # 140703195123584
# ascii() 与 repr() 类似，返回一个包含对象的可打印表示的字符串，但 repr() 返回的非 ASCII 字符会用 \x、\u 或 \U 转义
print(ascii('123'))  # 123
# bin() 将整数转换为以“0b”为前缀的二进制字符串
print(bin(123))  # 0b1111011
# bytes() 返回一个新的“bytes”对象，它是一个不可变的整数序列，范围是 0 <= x < 256
print(bytes('123', encoding='utf-8'))  # b'123'
# ord() 对于 bytes 对象中的单个字节，返回其整数值
print(ord(b'1'))  # 49
# exec() 此函数支持动态执行 Python 代码。object 必须是字符串或代码对象
print(exec('print(123)'))  # 123
# compile() 将 source 编译为代码或 AST 对象。代码对象可以由 exec() 或 eval() 执行
print(compile('print(123)', '', 'exec'))  # True
# help() 交互式帮助系统
print(help(str))  # <class 'str'>
# input() 读取一行输入，返回字符串
print(input('请输入一个数字: '))  # 123
# isinstance() 如果对象是指定类的实例，或者对象是该类的子类的实例，则返回 True
print(isinstance(123, int))  # True
# issubclass() 如果类是指定类的子类，则返回 True
print(issubclass(bool, int))  # True
# len() 返回对象（字符串、列表、元组、字典等）的长度
print(len('hello'))  # 5
# list() 将可迭代对象转换为列表
print(list('hello'))  # ['h', 'e', 'l', 'l', 'o']
# locals() 返回当前作用域的局部变量字典
print(locals())  # {'__name__': '__main__', '__doc__': None, ...}
# map() 返回一个迭代器，应用于 iterable 的每个元素的函数
print(map(lambda x: x * 2, [1, 2, 3]))  # <map object at 0x7f8c8c0d3f40>
# max() 返回可迭代对象中的最大值
print(max([1, 2, 3]))  # 3
# min() 返回可迭代对象中的最小值
print(min([1, 2, 3]))  # 1
# next() 返回迭代器的下一个项目
print(next(iter([1, 2, 3])))  # 1
# oct() 将整数转换为以“0o”为前缀的八进制字符串
print(oct(8))  # 0o10
# open() 打开文件并返回文件对象
# with open('test.txt', 'w') as f:
#     f.write('Hello, world!')
#
# ord() 返回字符串中第一个字符的 Unicode 码位
print(ord('a'))  # 97
# pow() 返回 x 的 y 次幂
print(pow(2, 3))  # 8 
# iter() 返回一个迭代器对象
print(iter([1, 2, 3]))  # <list_iterator object at 0x7f8c8c0d3f40>
# range() 返回一个可迭代对象
print(range(5))  # range(0, 5)
# round() 返回浮点数 x 的四舍五入值
print(round(3.14159, 2))  # 3.14
# sorted() 返回一个排序列表
print(sorted([3, 1, 2]))  # [1, 2, 3]
# str() 将对象转换为字符串
print(str(123))  # '123'
# sum() 返回可迭代对象中所有元素的和
print(sum([1, 2, 3]))  # 6 
# tuple() 将可迭代对象转换为元组
print(tuple([1, 2, 3]))  # (1, 2, 3)
# type() 返回对象的类型
print(type(123))  # <class 'int'>
# zip() 返回一个迭代器，聚合来自每个可迭代对象的元素
print(zip([1, 2, 3], ['a', 'b', 'c']))  # <zip object at 0x7f8c8c0d3f40>
# isinstance() 检查对象是否是指定类的实例
print(isinstance(123, int))  # True
# issubclass() 检查类是否是指定类的子类
print(issubclass(bool, int))  # True
# memoryview() 返回给定参数的内存视图对象
print(memoryview(bytes('123', encoding='utf-8')))  # <memory at 0x7f8c8c0d3f40>
# globals() 返回当前全局符号表的字典
print(globals())  # {'__name__': '__main__', '__doc__': None, ...}
# object() 返回一个新的“空”对象
print(object())  # <object object at 0x7f8c8c0d3f40>
# slice() 返回一个 slice 对象
print(slice(1, 5))  # slice(1, 5, None)
# property() 返回一个 property 对象
print(property())  # <property object at 0x7f8c8c0d3f40>
