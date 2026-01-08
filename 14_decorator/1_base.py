from functools import wraps

# 装饰器会丢失原函数的元信息（如__name__），使用functools.wraps可以修复：
# 装饰器的wrapper函数必须与原函数参数兼容，使用*args, **kwargs可以处理任意参数：
# 如果有多个装饰器原理一样，套娃，最上边的就是套娃的最外层
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("日志开始")
        func(*args, **kwargs)
        print("日志结束")
    return wrapper

@log
def buy(id):
    print(f"buy a apple, id is {id}")
    
buy(10)

# 带参数的装饰器
def record(level):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("开始say")
            if level == "10":
                print(f"普通话{level}级")
            func(*args, **kwargs)
            print("结束say")
        return wrapper
    return decorator

@record(level="10")
def say(content):
    print(f"You say {content}")
    
say("what's fuck!")