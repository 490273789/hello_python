"""
类：
    类是对大量对象共性的抽象
        有什么：属性
        能做什么：方法
    在程序中，类是创建对象的模版
    类是客观事物在人脑中的主管反应
对象：
    在自然界中，只要是客观存在的事物都是对象（万物皆对象）
类的组成：

    属性：
        类属性
        实例属性
    方法：
        类方法
        实例方法
        静态方法
        特殊方法（魔法方法）
"""


# 创建一个动物类
class Animal:
    """
    类的说明对象
    self：
        1.作为实例传参
            self作为实例自身，调用类方法的时候，会作为第一个参数传入，
            因此当我们调用p.eat(),就相当于Person.eat(p)
        2.调用类的实例属性和实例方法
    类属性：
        类中所有实例共享这个属性
        类属性：也叫做类变量，在类中方法外定义
        通过 类名.属性名 或 实例.属性名（如果实例属性名没有覆盖类属性名） 访问
        通过 类型.属性名的方式添加或修改类属性名
    实例属性：
        在__init__中通过self. 定义的属性
        虽然在类中定义，但是在实例中有各自的值，互相之间不影响


    """

    home = "森林"

    # 实例属性和方法
    def __init__(self, name, species):
        """
        构造函数
        所有的实力属性都定义在此方法中
        不需要显示的调用，在创建对象的时候自动调用__init__方法
        不是必须写，不写会调用底层默认的__init__方法，没有任何类属性
        此方法，只能返回None，如果尝试返回其他值，会报错：TypeError
        """
        self._name = name  # 实例属性 _name 以单下划线开头，表示这是一个受保护的属性，没有实际的语法约束，算是约定俗成的
        self.species = species
        self.__age = 0  # 实例属性 __age 以双下划线开头，表示这是一个私有属性
        self._weight = 0.0

    def get_age(self):
        """
        实例方法：
            在类中定义，第一个参数是self，代表实例本身
            实例方法只能被实例对象调用
            可以访问实例属性、类属性、类方法
        """
        print(f"{self._name}'s age is {self.__age}")
        return self.__age

    def set_age(self, age):
        if age >= 0 and age <= 150:  # 假设年龄范围是0到150岁
            self.__age = age
        else:
            print("Age cannot be negative.")

    # 使用@property装饰器可以将方法转换为属性, 直接可以使用 实例.属性 的方式访问
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age >= 0 and age <= 150:  # 假设年龄范围是0到150岁
            self.__age = age
        else:
            print("Age cannot be negative.")

    # 特殊方法
    def __make_sound(self, sound):
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
        print(f"{self._name} says: {sound}")

    # 类方法
    @classmethod
    def get_zoo_count(cls):
        """
        类方法：
            在类中通过@classmethod定义，第一个参数cls，代表类本身
            类方法可以被类和实例对象调用
            可以访问属性
            在不创建实例的情况下调用，通过类型直接调用
        """
        return cls.numbers

    # 静态方法
    @staticmethod
    def add(a, b):
        """
        静态方法
            在类中通过@staticmethod定义
            不访问类属性和实例属性，只依赖于，传入的参数
            可以通过类名或实例调用，不会访问类或实例的内部信息，更像工具方法，为了方便组织代码，放在类里面

        """
        return a + b


animal = Animal("吞吞", "饕餮")
animal.get_age()  # 低层实现： Animal.get_age(animal)
Animal.get_age(animal)
animal.home = "树林"  # 这种方式，无法修改类属性，而是添加一个新的实例属性
print(Animal.home, animal.home)
