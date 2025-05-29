# 魔法方法
#  魔法方法是 Python 中的一种特殊方法，它们以双下划线开头和结尾（例如 `__init__`）。这些方法允许我们定义类的行为，例如如何创建对象、如何表示对象、如何比较对象等。
class User:
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