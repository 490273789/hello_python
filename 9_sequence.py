from functools import reduce
# 序列
# 序列是 Python 中的一种数据类型，成员是有序排列的，可以通过索引访问。
# 序列的类型有：列表、元组、字符串等
# 列表
my_list = [1, 2, 3, 4, 5]
print(my_list)
# 元组
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# 字符串
my_string = "Hello, World!"
print(my_string)

# 序列的通用操作
# 访问元素
print(my_list[0])
print(my_tuple[0])
print(my_string[0])
# 切片
print(my_list[1:3])
print(my_tuple[1:3])
print(my_string[1:5])
# 迭代
for item in my_list:
    print(item)
for item in my_tuple:
    print(item)
for char in my_string:
    print(char)
# len() 计算容器中元素数量
print(len(my_list))

# del(item) 删除变量
# max(item) 返回最大值
# min(item) 返回最小值

# 序列通用的操作
# + 连接两个序列
print(my_list + my_list)
# * 重复序列
print(my_list * 2)
# in 判断元素是否在序列中
print(1 in my_list)
# not in 判断元素是否不在序列中
print(6 not in my_list)
# index() 返回元素的索引
print(my_list.index(3))
# count() 返回元素的数量
print(my_list.count(3))
# list() 将其他序列转换为列表
print(list(my_tuple))
# tuple() 将其他序列转换为元组
print(tuple(my_list))
# str() 将其他序列转换为字符串
print(str(my_list))
# sorted() 返回排序后的序列
print(sorted(my_list))
# reversed() 返回反转后的序列
print(list(reversed(my_list)))
# join() 将序列中的元素连接成字符串
print(", ".join(map(str, my_list)))
# split() 将字符串分割成序列
print(my_string.split(", "))
# enumerate() 返回序列的索引和元素
for index, item in enumerate(my_list):
    print(index, item)
# zip() 将多个序列组合成一个序列
my_list2 = [6, 7, 8]
for item1, item2 in zip(my_list, my_list2):
    print(item1, item2) 
# map() 将函数应用于序列中的每个元素
def square(x):
    return x * x
print(list(map(square, my_list)))
# filter() 过滤序列中的元素
def is_even(x):
    return x % 2 == 0
print(list(filter(is_even, my_list)))

# reduce() 将函数应用于序列中的每个元素，返回一个值
def add(x, y):
    return x + y
print(reduce(add, my_list))

# 删除序列
sequence_1 = (1,2,3,4,5)
del sequence_1 # 删除整个元组

# 比较运算符
# == 判断两个序列是否相等
print(my_list == my_list2)
# != 判断两个序列是否不相等
print(my_list != my_list2)
# < 判断序列是否小于另一个序列
print(my_list < my_list2)
# <= 判断序列是否小于等于另一个序列
print(my_list <= my_list2)
# > 判断序列是否大于另一个序列
print(my_list > my_list2)
# >= 判断序列是否大于等于另一个序列
print(my_list >= my_list2)