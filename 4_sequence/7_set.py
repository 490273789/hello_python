# set 不允许有重复元素
# set 是无序的，没有索引，所以不能进行切片操作，与dict类似，是key的集合

# set的创建
set_var = {1, 2, 3, 4, 5}
print("set_var:", set_var)  # {1, 2, 3, 4, 5}

set_var1 = set()
print("set_var1:", set_var1)  # {}
# list to set
set_var2 = set([1, 2, 3, 4, 5, 1, 2])
print("set_var2:", set_var2)  # {1, 2, 3, 4, 5}

# set推导式
set_var2 = {i * 2 for i in range(10)}
print(f"set_var2: {set_var2}")

# tuple to set
set_var3 = set((1, 2, 3, 4, 5, 1, 2))
print("set_var3:", set_var3)  # {1, 2, 3, 4, 5}
# 字符串 to set
set_var4 = set("hello")
print("set_var4:", set_var4)  # {'h', 'e', 'l', 'o'}
# dict to set
set_var5 = set({"a": 1, "b": 2, "c": 3})
print("set_var5:", set_var5)  # {'a', 'b', 'c'}
# in
print("a in set_var5:", "a" in set_var5)  # True
print("d in set_var5:", "d" in set_var5)  # False
# not in
print("a not in set_var5:", "a" not in set_var5)  # False
print("d not in set_var5:", "d" not in set_var5)  # True
# set的长度
print("set_var length:", len(set_var))  # 5
# set的清空
# set_var.clear()
# print("set_var:", set_var)  # set()
# set的复制
set_var = {1, 2, 3, 4, 5}
set_var_copy = set_var.copy()
print("set_var_copy:", set_var_copy)  # {1, 2, 3, 4, 5}
# set的更新
set_var.update({6, 7, 8})  # 参数需要是可迭代对象
print("set_var:", set_var)  # {1, 2, 3, 4, 5, 6, 7, 8}
# set的添加
set_var.add(6)
print("set_var:", set_var)  # {1, 2, 3, 4, 5, 6}
# set的删除
set_var.remove(3)  # 从集合中删除元素，元素不存在会报错
print("set_var:", set_var)  # {1, 2, 4, 5, 6}

set_var.discard(10)  # 从集合中删除元素，元素不存在也不会报错
# set的遍历
for item in set_var:
    print("item:", item)
# set的长度
print("set_var length:", len(set_var))  # 5
# set的交集
set_var1 = {1, 2, 3}
set_var2 = {3, 4, 5}
print("set_var1 & set_var2:", set_var1 & set_var2)  # {3}
# set的并集
print("set_var1 | set_var2:", set_var1 | set_var2)  # {1, 2, 3, 4, 5}
# set的差集
print(
    "set_var1 - set_var2:", set_var1 - set_var2
)  # {1, 2} 1, 2在set_var1中但不在set_var2中
# set的对称差集
print("set_var1 ^ set_var2:", set_var1 ^ set_var2)  # {1, 2, 4, 5}
# set的子集
print("set_var1 <= set_var2:", set_var1 <= set_var2)  # False
# set的超集
print("set_var1 >= set_var2:", set_var1 >= set_var2)  # False

# set del
del set_var1
# print("set_var1:", set_var1)  # NameError: name 'set_var1' is not defined
