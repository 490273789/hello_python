# 魔法方法
# 魔法方法是 Python 中的一种特殊方法，它们以双下划线开头和结尾（例如 `__init__`）。
# 这些方法允许我们定义类的行为，例如如何创建对象、如何表示对象、如何比较对象等。


class User:
    """
    特殊方法（魔法方法）：方法名中有两个特殊的前缀__和后缀__的方法
    这些方法会在进行特殊操作时，自动被调用
    __new__(): 对象实例化时第一个调用的方法
    __init__(): 类的初始化方法
    __del__(): 对象销毁器，定义了当对象被垃圾回收时的行为，使用delXXX时不会主动带调用__del__,除非此时引用计数==0
    __str__(): 定义了对类的实例调用str是的行为
    __repr__(): 定义对类的实例调用repr()时的行为。str和repr最主要的差别是在于目标用户。
        repr()的作用是产生机器可读的输出
        str() 则产生人类可读的输出
    __getattribute__(): 属性访问拦截器，定义了属性被访问前的操作
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 重写默认的字符串表示方法
    def __str__(self):
        return f"User(name={self.name}, age={self.age})"

    # 重写默认的表示方法
    def __repr__(self):
        return f"User({self.name!r}, {self.age!r})"

    # 重写比较方法
    def __eq__(self, other):
        if isinstance(other, User):
            return self.name == other.name and self.age == other.age
        return False

    #  重写加法操作符
    def __add__(self, other):
        if isinstance(other, User):
            return User(self.name + " & " + other.name, self.age + other.age)
        return NotImplemented

    # 重写长度方法
    def __len__(self):
        return len(self.name) + self.age
