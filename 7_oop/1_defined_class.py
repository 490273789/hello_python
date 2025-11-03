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
    实例方法：
        在类中定义，第一个参数是self，代表实例本身
        实例方法只能被实例对象调用
        可以访问实例属性、类属性、类方法
    类方法：
        在类中通过@classmethod定义，第一个参数cls，代表类本身
        类方法可以被类和实例对象调用
        可以访问属性
        在不创建实例的情况下调用，通过类型直接调用
    静态方法
        在类中通过@staticmethod定义
        不访问类属性和实例属性，只依赖于，传入的参数
        可以通过类名或实例调用，不会访问类或实例的内部信息，更像工具方法，为了方便组织代码，放在类里面

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

    # 方法名也可以用__开头，表示这是一个私有方法
    def __make_sound(self, sound):
        print(f"{self._name} says: {sound}")


animal = Animal("吞吞", "饕餮")
animal.get_age()  # 低层实现： Animal.get_age(animal)
Animal.get_age(animal)
animal.home = "树林"  # 这种方式，无法修改类属性，而是添加一个新的实例属性
print(Animal.home, animal.home)


# 创建一个狗类，继承自动物类
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")  # 继承
        self.breed = breed

    def wag_tail(self):
        print(f"{self._name} is wagging its tail.")


# 创建一个猫类，继承自动物类
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def purr(self):
        print(f"{self._name} is purring.")


# 创建一个动物园类，包含多个动物
class Zoo:
    # 已构建动物园数量
    numbers = 0  # 类属性
    # 最多可养动物数量
    max_animals = 3  # 类属性

    # 初始化方法
    def __init__(self):
        self.animals = []  # 实例属性
        Zoo.numbers += 1

    # 类方法
    @classmethod
    def get_zoo_count(cls):
        return cls.numbers

    # 实例方法
    def add_animal(self, animal):
        if len(self.animals) < Zoo.max_animals:
            self.animals.append(animal)
        else:
            print("无法添加更多动物，已达到最大数量。")

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal._name} is a {animal.species}.")
            if isinstance(animal, Dog):
                animal.wag_tail()
            elif isinstance(animal, Cat):
                animal.purr()

    # 静态方法
    @staticmethod
    def get_max_animals():
        return Zoo.max_animals


# 创建动物园实例
zoo = Zoo()
# 添加动物
zoo.add_animal(Dog(name="Buddy", breed="Golden Retriever"))
zoo.add_animal(Cat(name="Whiskers", color="Tabby"))
# 显示动物
zoo.show_animals()

# 动物园数量
print(f"Total number of zoos: {Zoo.numbers}")  # 输出: Total number of zoos: 1

# 调用类方法
print(f"Total number of zoos: {Zoo.get_zoo_count()}")  # 输出: Total number of zoos: 1
# 输出:
# Buddy is a Dog.
# Buddy is wagging its tail.
# Whiskers is a Cat.
# Whiskers is purring.
# 这个示例展示了如何定义类、继承和多态。
# 通过创建一个动物园类来管理多个动物实例。
print(type(zoo))  # <class '__main__.Zoo'>
print(isinstance(zoo, Zoo))  # True
print(isinstance(zoo, Animal))  # False

# __dict__ 属性可以查看对象的属性
print(
    zoo.__dict__
)  # {'animals': [<__main__.Dog object at ...>, <__main__.Cat object at ...>]}
# __class__ 属性可以查看对象的类
print(zoo.__class__)  # <class '__main__.Zoo'>
# __module__ 属性可以查看对象所在的模块
print(zoo.__module__)  # __main__
# __name__ 属性可以查看对象的名称
print(zoo.__class__.__name__)  # Zoo
# __bases__ 属性可以查看类的基类
print(zoo.__class__.__bases__)  # (<class 'object'>,)
# __doc__ 属性可以查看类的文档字符串
print("zoo.__class__.__doc__:", zoo.__class__.__doc__)  # None, 因为没有定义文档字符串
print("Zoo.__doc__:", Zoo.__doc__)  # None, 因为没有定义文档字符串

# dir() 函数可以查看对象的所有属性和方法
print(dir(zoo))  # 查看 zoo 对象的所有属性和方法
