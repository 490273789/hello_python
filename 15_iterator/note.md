## 1. 基本概念

1. Iterable（可迭代对象）  
   - 含有 `__iter__()` 方法，调用后返回一个 iterator；或实现了按序访问的旧协议 `__getitem__(index)`（从 0 开始，直到抛出 `IndexError`）。
   - 常见：`list`, `tuple`, `str`, `dict`, `set`, `range`, 自定义类等。

2. Iterator（迭代器对象）  
   - 同时实现：
     - `__iter__()`：返回自身（`return self`）
     - `__next__()`：返回下一个元素；无元素时抛出 `StopIteration`
   - 迭代器是“惰性”的（lazy），只在需要时生成数据。

3. for 循环的内部机制（伪过程）：
```python
_iter = iter(obj)           # 调用 obj.__iter__()
while True:
    try:
        item = next(_iter)  # 调用 _iter.__next__()
    except StopIteration:
        break
    # 使用 item
```

---

## 2. 判定一个对象是否可迭代 / 迭代器

```python
from collections.abc import Iterable, Iterator

def inspect(obj):
    print(type(obj), 'Iterable?', isinstance(obj, Iterable), 'Iterator?', isinstance(obj, Iterator))

inspect([1, 2, 3])     # list: Iterable True, Iterator False
inspect(iter([1, 2]))  # list_iterator: Iterable True, Iterator True
inspect(range(5))      # range: Iterable True, Iterator False
inspect((x for x in range(3)))  # generator: Iterable True, Iterator True
```

---

## 3. 自定义迭代器类

```python
class Countdown:
    """从 n 倒数到 1 的迭代器"""
    def __init__(self, n: int):
        self.current = n

    def __iter__(self):
        return self  # 自身就是迭代器

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for num in Countdown(5):
    print(num, end=' ')
# 输出: 5 4 3 2 1
```

注意：迭代器“一次性”消费，耗尽后需重新创建实例。

---

## 4. 可迭代但不是迭代器的类（分离 Iterator 对象）

```python
class CountdownIterable:
    """可反复迭代（每次 for 都重新开始）"""
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        # 每次返回一个新的迭代器对象
        return CountdownIterator(self.n)

class CountdownIterator:
    def __init__(self, n):
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

c = CountdownIterable(3)
print(list(c))  # [3, 2, 1]
print(list(c))  # 再次可用 [3, 2, 1]
```

---

## 5. 生成器（Generator）

生成器是创建迭代器的最常用方式，语法简洁。

### 5.1 `yield` 生成器函数

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print(list(countdown(5)))  # [5, 4, 3, 2, 1]
```

生成器函数调用后返回一个生成器对象（即迭代器）。

### 5.2 `yield from` 委托

```python
def flatten(list_of_lists):
    for sub in list_of_lists:
        yield from sub   # 等价于: for x in sub: yield x

print(list(flatten([[1, 2], (3, 4), "ab"])))  # [1, 2, 3, 4, 'a', 'b']
```

### 5.3 生成器表达式

```python
gen = (x * x for x in range(5))
print(next(gen))  # 0
print(list(gen))  # 剩余: [1, 4, 9, 16]
```

---

## 6. StopIteration 与返回值

生成器结束时可以用 `return value`，该值会作为 `StopIteration.value` 保存。

```python
def compute_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
        yield i
    return total

g = compute_sum(5)
for v in g:
    print(v)
# 想拿 return 的值：
g = compute_sum(5)
try:
    while True:
        next(g)
except StopIteration as e:
    print('sum =', e.value)  # sum = 15
```

---

## 7. 可重复迭代 vs 只能一次

- 可重复：容器类（list, range, dict 等），每次 iter() 返回新的迭代器。
- 只能一次：生成器、文件句柄、迭代器对象本身。

常见 Bug：对一个生成器做两次遍历，第二次为空。

```python
g = (x for x in range(3))
print(list(g))  # [0, 1, 2]
print(list(g))  # []
```

---

## 8. `iter()` 的两种形式

1. `iter(obj)`：获取对象的迭代器。
2. `iter(callable, sentinel)`：不断调用 `callable()`，直到其返回 `sentinel` 停止。

```python
import random

def roll():
    return random.randint(1, 6)

for v in iter(roll, 6):  # 直到 roll() 返回 6
    print(v)
```

---

## 9. `next()` 的默认值参数

```python
it = iter([1, 2])
print(next(it))               # 1
print(next(it))               # 2
print(next(it, 'END'))        # 'END'（不会抛异常）
```

---

## 10. 常用工具：`itertools` 模块

```python
import itertools as it

# 无限迭代器
counter = it.count(start=10, step=2)
print(next(counter), next(counter), next(counter))  # 10 12 14

# cycle / repeat
cyc = it.cycle('AB')
print([next(cyc) for _ in range(5)])  # ['A', 'B', 'A', 'B', 'A']

print(list(it.islice(it.repeat('X'), 5)))  # ['X', 'X', 'X', 'X', 'X']

# 链接
print(list(it.chain([1, 2], ('a', 'b'))))  # [1, 2, 'a', 'b']

# 组合与排列
print(list(it.combinations([1, 2, 3], 2)))  # [(1, 2), (1, 3), (2, 3)]
print(list(it.permutations('ABC', 2)))      # [('A','B'), ('A','C'), ...]

# 分组
for k, group in it.groupby('aaabbcaaa'):
    print(k, list(group))
# a ['a','a','a']
# b ['b','b']
# c ['c']
# a ['a','a','a']

# 压缩与过滤
print(list(it.compress('abcdef', [1, 0, 1, 0, 0, 1])))  # ['a','c','f']

# 累计
print(list(it.accumulate([1, 2, 3, 4])))  # [1, 3, 6, 10]

# 短路拉链
print(list(it.zip_longest([1,2], ['a'], fillvalue='?')))  # [(1,'a'), (2,'?')]
```

---

## 11. 惰性（Lazy）与内存效率

使用迭代器可以避免一次性加载大数据。示例：读取大文件行处理。

```python
def read_large_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:       # 文件对象自身就是迭代器
            yield line.rstrip('\n')

# 惰性处理
for line in read_large_file('big.txt'):
    if 'ERROR' in line:
        print(line)
```

---

## 12. 管道式（Pipeline）迭代

```python
def gen_numbers():
    for i in range(1, 20):
        yield i

def even_only(iterable):
    for x in iterable:
        if x % 2 == 0:
            yield x

def square(iterable):
    for x in iterable:
        yield x * x

pipeline = square(even_only(gen_numbers()))
print(list(pipeline))  # [4, 16, 36, 64, 100, 144, 196, 256, 324]
```

---

## 13. 可迭代解包、星号等操作如何触发迭代

```python
a, b, *rest = range(6)
print(a, b, rest)  # 0 1 [2,3,4,5]
```

---

## 14. enumerate / zip 等组合迭代器

```python
for idx, val in enumerate(['a', 'b', 'c'], start=1):
    print(idx, val)

for a, b in zip([1, 2, 3], ['x', 'y', 'z']):
    print(a, b)
```

注意：`zip` 返回迭代器；在 Python 2 中返回列表（历史差异）。

---

## 15. 迭代器耗尽的常见陷阱

```python
def data():
    print("生成数据")
    for i in range(3):
        print(" yield", i)
        yield i

g = data()
# 第一次消费
sum1 = sum(g)
# 第二次消费为空
sum2 = sum(g)

print(sum1, sum2)  # 3 0
```

解决方案：如果需多次使用结果，转换成列表或重新生成。

---

## 16. 复制迭代器（itertools.tee）

```python
import itertools as it

g = (x * 2 for x in range(5))
g1, g2 = it.tee(g, 2)
print(list(g1))  # [0,2,4,6,8]
print(list(g2))  # [0,2,4,6,8]
```

注意：`tee` 会缓存已消费元素，过度使用可能占用内存。

---

## 17. 自定义惰性无限序列（斐波那契）

```python
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

import itertools as it
print(list(it.islice(fib(), 10)))  # 前10项
```

---

## 18. 异步迭代器 / 异步生成器（进阶）

Python 3.6+ 支持 `async for` 与 `async def ... yield`

```python
import asyncio
import random

class AsyncCounter:
    def __init__(self, n):
        self.n = n

    def __aiter__(self):
        self.current = 0
        return self

    async def __anext__(self):
        if self.current >= self.n:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        self.current += 1
        return self.current

async def main():
    async for val in AsyncCounter(3):
        print(val)

asyncio.run(main())
```

异步生成器：

```python
async def agen():
    for i in range(3):
        yield i

# async for i in agen(): ...
```

---

## 19. 性能与最佳实践

1. 优先使用生成器表达式 / 迭代器，减少内存压力。  
2. 需要随机访问或多次遍历 → 用列表或缓存。  
3. 链式操作时注意可读性，可引入函数式组合或注释。  
4. 不要滥用 `tee`；必要时转 `list`.  
5. 当需要“看一眼”数据再继续迭代，可使用 `itertools.islice` 或 `more_itertools.peekable`（第三方）。  

---

## 20. 实战例子：流式处理日志统计

```python
def read_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')

def filter_error(lines):
    for line in lines:
        if 'ERROR' in line:
            yield line

def parse_code(lines):
    for line in lines:
        # 假设格式: "[ERROR] <code> message"
        if line.startswith('[ERROR]'):
            parts = line.split()
            yield parts[1]  # 取错误码

from collections import Counter

def top_errors(path, n=5):
    codes = parse_code(filter_error(read_lines(path)))
    counter = Counter(codes)
    return counter.most_common(n)

# 使用:
# print(top_errors('app.log', 10))
```

---

## 21. 快速自查列表

| 目标 | 推荐方式 |
|------|----------|
| 创建简单一次性序列 | 生成器函数 (`yield`) |
| 多次迭代 | 实现 `__iter__` 返回新迭代器 或 直接用容器 |
| 惰性大数据 | 迭代器 / 生成器 |
| 多来源拼接 | `itertools.chain` |
| 截取前 N 个 | `itertools.islice(iterable, N)` |
| 无限序列 | 自定义生成器 / `itertools.count` |
| 多进程/IO并行 | 考虑 `async for` 或并发工具 |
| 同时遍历多个序列 | `zip` / `zip_longest` |
| 复制迭代流 | `itertools.tee`（谨慎） |

---

## 22. 综合练习：管道+统计+惰性

```python
import re
from collections import Counter
import itertools as it

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.lower()

def words(lines):
    pattern = re.compile(r'[a-z]+')
    for line in lines:
        for w in pattern.findall(line):
            yield w

def sliding_window(iterable, size=2):
    it1, it2 = it.tee(iterable)
    for _ in range(size - 1):
        it2 = it.islice(it2, 1, None)
    # 构造窗口
    while True:
        try:
            win = [next(it1)]
            rest = []
            temp = it2
            for _ in range(size - 1):
                val = next(temp)
                rest.append(val)
            yield tuple([win[0]] + rest)
            it1, it2 = it.tee(it1)
            it2 = it.islice(it2, 1, None)
        except StopIteration:
            break

def top_bigrams(path, topn=5):
    ws = words(read_file(path))
    bigrams = zip(ws, ws)  # 简单成对（非真实滑窗）
    counter = Counter(bigrams)
    return counter.most_common(topn)

# print(top_bigrams('book.txt'))
```

---

## 23. 什么时候不该用迭代器

1. 需要频繁随机访问（索引）  
2. 需要长度（但可以通过 `collections.abc.Sized` / `len()` 提供）  
3. 需要多次完整遍历且生产成本高（可缓存）  

---

## 24. 小测验（自检）

试着回答：
1. `range(10)` 是迭代器吗？
2. 判断一个对象是不是迭代器要检查哪些方法？
3. 如何实现一个可以无限生成斐波那契的惰性序列？
4. `iter(callable, sentinel)` 的用途是什么？
5. 为什么对同一个生成器做两次 `for` 第二次不输出结果？

（可回头对照上文验证）

---

## 25. 总结要点

- Iterable 提供可迭代能力，Iterator 提供逐步获取值的协议。  
- 生成器是实现迭代器最简洁的方法。  
- `for` / 解包 / 推导式 / `zip` / `enumerate` 等都基于迭代协议。  
- 惰性使得处理大数据、流式数据更高效。  
- 注意“迭代器一次性”与副作用。  
- 熟练掌握 `itertools` 是写出高效 Python 的关键一环。  

---
