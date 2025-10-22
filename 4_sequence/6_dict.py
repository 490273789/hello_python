# dictionary 字典
# key是唯一的
# 无序（3.7+ 版本保持插入顺序）
dict_var = {"name": "Alice", "age": 30, "city": "New York"}
dict_var2 = dict(name="Alice", age=30, city="New York")
print("dict_var:", dict_var)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
# 字典的访问 查询不存在的key会报错
print("dict_var['name']:", dict_var["name"])  # Alice
print("dict_var['age']:", dict_var["age"])  # 30
print("dict_var['city']:", dict_var["city"])  # New York
# get() 获取字典的值
dict_var = {"name": "Alice", "age": 30, "city": "New York"}
print("dict_var.get('name'):", dict_var.get("name"))  # Alice
print("dict_var.get('job'):", dict_var.get("job"))  # None. 查询不存在的Key不会报错
# 字典的添加
dict_var["job"] = "Engineer"
print(
    "dict_var:", dict_var
)  # {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}
# 字典的修改
dict_var["age"] = 31
print(
    "dict_var:", dict_var
)  # {'name': 'Alice', 'age': 31, 'city': 'New York', 'job': 'Engineer'}
# 字典的删除
del dict_var["city"]
print("dict_var:", dict_var)  # {'name': 'Alice', 'age': 31, 'job': 'Engineer'}
# 字典的遍历
for key in dict_var:
    print("key:", key)  # name age job
# items()
for key, value in dict_var.items():
    print("key:", key, "value:", value)
# keys()
for key in dict_var.keys():
    print("key:", key)  # name age job
# values()
for value in dict_var.values():
    print("value:", value)  # Alice 31 Engineer
# 字典的长度
print("dict_var length:", len(dict_var))  # 3

# 字段的常用方法
# clear() 清空字典
dict_var.clear()
print("dict_var:", dict_var)  # {}
# copy() 复制字典
dict_var = {"name": "Alice", "age": 30, "city": "New York"}
dict_var_copy = dict_var.copy()
print(
    "dict_var_copy:", dict_var_copy
)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
# fromkeys() 创建字典
dict_var = dict.fromkeys(["name", "age", "city"], "unknown")
print("dict_var:", dict_var)  # {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}

# pop() 删除字典的键值对
dict_var = {"name": "Alice", "age": 30, "city": "New York"}
print("dict_var.pop('age'):", dict_var.pop("age"))  # 30
print("dict_var:", dict_var)  # {'name': 'Alice', 'city': 'New York'}
# popitem() 删除字典的最后一个键值对
dict_var = {"name": "Alice", "age": 30, "city": "New York"}
print("dict_var.popitem():", dict_var.popitem())  # ('city', 'New York')
print("dict_var:", dict_var)  # {'name': 'Alice', 'age': 30}
# setdefault() 设置默认值
dict_var = {"name": "Alice", "age": 30}
print(
    "dict_var.setdefault('job', 'Engineer'):", dict_var.setdefault("job", "Engineer")
)  # Engineer
print("dict_var:", dict_var)  # {'name': 'Alice', 'age': 30, 'job': 'Engineer'}
# update() 更新字典
dict_var = {"name": "Alice", "age": 30}
dict_var.update({"city": "New York", "job": "Engineer"})
print(
    "dict_var:", dict_var
)  # {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}
# 字典的嵌套
dict_var = {"name": "Alice", "age": 30, "address": {"city": "New York", "state": "NY"}}
print("dict_var['address']['city']:", dict_var["address"]["city"])  # New York
# 字典的排序
dict_var = {"name": "Alice", "age": 30, "city": "New York"}
sorted_dict = dict(sorted(dict_var.items(), key=lambda item: item[0]))
print("sorted_dict:", sorted_dict)  # {'age': 30, 'city': 'New York', 'name': 'Alice'}
# 字典的合并
dict_var1 = {"name": "Alice", "age": 30}
dict_var2 = {"city": "New York", "job": "Engineer"}
dict_var1.update(dict_var2)
print(
    "dict_var1:", dict_var1
)  # {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}
# 字典的推导式
dict_var = {x: x**2 for x in range(5)}
print("dict_var:", dict_var)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# 字典的嵌套推导式
dict_var = {x: {y: x * y for y in range(3)} for x in range(3)}
print(
    "dict_var:", dict_var
)  # {0: {0: 0, 1: 0, 2: 0}, 1: {0: 0, 1: 1, 2: 2}, 2: {0: 0, 1: 2, 2: 4}}
