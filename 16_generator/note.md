## 1. 背景：迭代器协议与生成器的地位

Python 中可迭代对象遵循迭代器协议：
- 可迭代对象需实现 `__iter__()` 返回一个迭代器。
- 迭代器需实现 `__next__()`，不断返回下一个值，耗尽后抛出 `StopIteration`。

生成器是 Python 自动帮你实现迭代器协议的一种快速方式：
- “生成器函数”：含 `yield` 的函数，调用后不会立即执行函数体，而是返回一个生成器对象。
- “生成器对象”：实现了迭代器协议，可用 `for`、`next()`、解包等方式消费。

---

## 2. 最基础示例：带 `yield` 的函数

```python
def count_up_to(n):
    """一个简单的生成器：从 1 数到 n"""
    i = 1
    while i <= n:
        yield i    # 暂停并输出当前值
        i += 1

gen = count_up_to(5)
print(gen)  # <generator object count_up_to at ...>

print(next(gen))  # 1
print(next(gen))  # 2

for x in gen:     # 继续消费剩余的 3,4,5
    print(x)
```

执行流程：遇到 `yield` 暂停，返回值给调用方，下次继续从暂停点往下执行。

---

## 3. 与返回列表的差别：惰性（Lazy）与节省内存

```python
def make_list(n):
    return [i for i in range(n)]

def make_gen(n):
    for i in range(n):
        yield i

lst = make_list(10_000_000)  # 占用大量内存
gen = make_gen(10_000_000)   # 几乎不占用（只是一个生成器对象）

import sys
print(sys.getsizeof(lst))  # 很大
print(sys.getsizeof(gen))  # 很小
```

生成器适合：
- 大数据流处理（日志、文件行、网络流）
- 无限序列（如斐波那契、产生随机数流）
- 链式数据管道

---

## 4. 生成器表达式 vs 列表推导式

```python
# 列表推导式：立刻构建整个列表
squares_list = [x * x for x in range(10)]

# 生成器表达式：惰性
squares_gen = (x * x for x in range(10))

print(squares_list)     # 立即看到全部
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
```

注意：生成器表达式外层若直接放在函数调用参数中，可省略外层括号：
```python
total = sum(x * x for x in range(10_000_000))
```

---

## 5. `yield` 与普通 `return` 的区别

- 普通函数 `return` 直接结束函数。
- 生成器函数中：
  - `yield` 暂停，保存当前栈帧状态。
  - 没有显式 `return` 或 `return` 不带值：迭代结束时抛 `StopIteration`，其 `value` 为 `None`。
  - `return value`：在生成器被耗尽时，抛出的 `StopIteration.value` 会携带该返回值（常用于协程/子生成器的结果传递）。

示例：

```python
def gen():
    yield 1
    yield 2
    return "done"

g = gen()
try:
    while True:
        print(next(g))
except StopIteration as e:
    print("生成器返回值：", e.value)
```

---

## 6. `send()`：向生成器“反向”发送数据（协程原型）

`send(value)` 会把 `yield` 表达式的结果替换为 `value`，继续执行。

```python
def accumulator():
    total = 0
    while True:
        x = yield total   # yield 当前累积值，并等待新值发送
        if x is None:      # 约定：None 不累积
            continue
        total += x

acc = accumulator()
print(next(acc))      # 0, 先“预激活”生成器至第一个 yield
print(acc.send(10))   # 10
print(acc.send(5))    # 15
print(acc.send(None)) # 15
print(acc.send(7))    # 22
```

预激活（priming）通常需要一个装饰器简化：

```python
def coroutine(func):
    def wrap(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)  # 预激活
        return g
    return wrap

@coroutine
def printer():
    while True:
        x = yield
        print("收到：", x)

p = printer()
p.send("Hello")
p.send("World")
```

---

## 7. `throw()` 与 `close()`

```python
def sample():
    try:
        while True:
            x = yield
            print("收到：", x)
    except GeneratorExit:
        print("生成器被关闭")

g = sample()
next(g)
g.send(1)
g.close()       # 触发 GeneratorExit
```

- `g.throw(exc_type, exc_value, traceback=None)`：在暂停处注入异常（测试、提前结束、错误传递）。
- `g.close()`：向生成器抛出 `GeneratorExit`，要求尽快结束；不要屏蔽它，不要再 `yield`。

---

## 8. `yield from`：子生成器委托机制

用途：
1. 自动迭代子生成器，无需手写循环。
2. 捕获子生成器的最终 `return value`。
3. 自动转发 `send()/throw()/close()`。

示例：扁平化 + 收集子生成器返回值。

```python
def subgen():
    yield 1
    yield 2
    return "sub-done"

def main():
    result = yield from subgen()
    print("子生成器返回值:", result)
    yield 3

for v in main():
    print("迭代得到:", v)
```

更复杂的协程管道：

```python
def child():
    total = 0
    while True:
        x = yield
        if x is None:
            break
        total += x
    return total

def parent():
    result = yield from child()
    print("子生成器统计结果:", result)

p = parent()
next(p)
p.send(10)
p.send(5)
p.send(None)   # 结束子生成器
```

---

## 9. 常见应用场景

1. 文件流处理：
```python
def read_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')
```

2. 管道化处理（组合多个生成器）：
```python
def numbers():
    for i in range(1, 10):
        yield i

def squared(seq):
    for x in seq:
        yield x * x

def even_only(seq):
    for x in seq:
        if x % 2 == 0:
            yield x

pipeline = even_only(squared(numbers()))
print(list(pipeline))  # [4, 16, 36, 64]
```

3. 无限序列：
```python
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

import itertools
print(list(itertools.islice(fib(), 10)))
```

4. 按需分页/批处理：
```python
def batched(iterable, size):
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch

print(list(batched(range(10), 3)))
```

---

## 10. 性能与注意事项

- 生成器减少内存占用，但不一定总是最快：频繁的 `yield` 切换有调用开销。
- 若需要随机访问、多次遍历，生成器不适合（被消费后无法回退）。
- 调试时可能遇到：`RuntimeError: generator raised StopIteration`（Python 3.7+ 已强化 PEP 479 行为，直接在生成器内部抛出 `StopIteration` 可能被转换为 `RuntimeError`，应使用 `return`）。
- 不要在生成器中吞掉 `GeneratorExit` 并继续 `yield`，否则会 `RuntimeError`.

---

## 11. 与迭代器类对比

手写迭代器类：

```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

print(list(CountDown(5)))
```

生成器写法：

```python
def countdown(start):
    while start > 0:
        yield start
        start -= 1

print(list(countdown(5)))
```

简洁度远胜手写迭代器类。

---

## 12. 调用栈与调试

使用 `yield` 的函数执行到第一次 `yield` 前不会真正进入后续语句，这让：
- 延迟计算
- 可以根据外部环境再决定是否继续

查看生成器状态：

```python
import inspect

def gen():
    x = 1
    y = yield x
    z = yield x + y
    return z

g = gen()
print(inspect.getgeneratorstate(g))  # GEN_CREATED
print(next(g))                       # 1
print(inspect.getgeneratorstate(g))  # GEN_SUSPENDED
```

四种状态：
- GEN_CREATED
- GEN_SUSPENDED
- GEN_RUNNING
- GEN_CLOSED

---

## 13. 捕获生成器返回值（配合 `yield from` 或手动）

```python
def worker():
    yield 1
    yield 2
    return 99

w = worker()
try:
    while True:
        v = next(w)
        print("值:", v)
except StopIteration as e:
    print("返回值:", e.value)
```

---

## 14. 异步生成器（简单了解）

Python 3.6+ 支持 `async def` + `yield` 形成“异步生成器”：
- 用于异步数据流（如网络事件、消息流）。
- 只能用 `async for` 消费。

```python
import asyncio

async def async_numbers():
    for i in range(3):
        await asyncio.sleep(0.5)
        yield i

async def main():
    async for v in async_numbers():
        print(v)

asyncio.run(main())
```

---

## 15. 综合示例：日志实时管道 + 过滤 + 统计

```python
def follow(path):
    """类似 tail -f，实时追踪文件新增行"""
    import time
    with open(path, 'r', encoding='utf-8') as f:
        f.seek(0, 2)  # 跳到文件尾
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.2)
                continue
            yield line.rstrip('\n')

def grep(keyword, lines):
    for line in lines:
        if keyword in line:
            yield line

def count(lines):
    total = 0
    for line in lines:
        total += 1
        yield total, line

# pipeline = count(grep("ERROR", follow("app.log")))
# for idx, line in pipeline:
#     print(f"{idx}: {line}")
```

---

## 16. 进阶技巧：双向通讯 + 子生成器的结果汇总

```python
def averager():
    total = 0.0
    count = 0
    avg = None
    while True:
        x = yield avg
        if x is None:  # 结束信号
            break
        count += 1
        total += x
        avg = total / count
    return avg

def group():
    results = {}
    while True:
        name = yield
        if name is None:
            break
        avg = yield from averager()
        results[name] = avg
    return results

def client():
    g = group()
    next(g)
    g.send("math")
    g.send(90)
    g.send(95)
    g.send(100)
    g.send(None)  # 结束 math
    g.send("english")
    g.send(80)
    g.send(85)
    g.send(None)  # 结束 english
    try:
        g.send(None)  # 结束 group
    except StopIteration as e:
        print("最终汇总:", e.value)

client()
```

---

## 17. 常见坑与建议

1. 忘记预激活协程：`send()` 前需先 `next()` 到第一个 `yield`。
2. 在生成器内直接抛 `StopIteration`：用 `return` 替代（PEP 479）。
3. 滥用生成器表达式：若需要多次遍历，应转成列表或缓存。
4. 生成器链过长调试困难：可在关键环节打印或使用日志。
5. 异常处理：在边界包装 try/except，不建议在每个小生成器内部深度嵌套。

---

## 18. 小测验（可自测）

```python
# 问题1：补全使函数返回所有偶数的平方（惰性）
def even_square(nums):
    # TODO: 使用生成器完成
    ...

# 问题2：写一个生成器，接收 send 过来的数字，返回当前最小值
def min_tracker():
    # TODO
    ...

# 问题3：实现一个批量读取文件行的生成器（每批 N 行）
def batched_lines(path, size):
    # TODO
    ...

# 可以自行尝试实现并测试。
```

---

## 19. 习题参考答案

```python
def even_square(nums):
    for n in nums:
        if n % 2 == 0:
            yield n * n

def min_tracker():
    current_min = None
    while True:
        x = yield current_min
        if x is None:
            continue
        if current_min is None or x < current_min:
            current_min = x

def batched_lines(path, size):
    batch = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            batch.append(line.rstrip('\n'))
            if len(batch) == size:
                yield batch
                batch = []
        if batch:
            yield batch
```

---

## 20. 总结要点速记

```text
- 含 yield 的函数 => 生成器函数，调用返回生成器对象
- 惰性计算，节省内存
- send() 传值进生成器，yield 表达式结果接收
- close() => GeneratorExit；throw() 注入异常
- return value 可通过 StopIteration.value 或 yield from 捕获
- yield from 用于子生成器委托与结果传递
- 适合流处理 / 无限序列 / 管道组合
```

---

如果你希望再深入某一部分（例如 async 生成器、协程模式、性能基准、调试技巧），告诉我，我可以继续展开。需要我把这些示例打包成文件格式也可以继续说明。祝学习愉快！