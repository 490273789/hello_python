# 元组 - 元组是不支持修改的序列，不能对元祖中的元素进行修改
# 元组是有序的，每个元素都有对应的下标（索引），可以通过索引获取元素，以及对元组进行切片
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# 元组的创建, 可以将其他的序列转换为元组
my_tuple1 = tuple([1, 2, 3, 4, 5])
print(my_tuple1)

# 注意元组只有一个元素的情况下的写法
my_single_tuple = (
    1,
)  # 如果不添加后面的逗号, 会被认为是一个整数，括号会被当做数学运算符
print(my_single_tuple)
# 元组的访问
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
# 元组的切片
print(my_tuple[1:3])
# 元组的迭代
for item in my_tuple:
    print(item)
# 元组的长度
print(len(my_tuple))
# 元组不支持添加

# 元组的删除
# del(my_tuple) # 删除整个元组
# del(my_tuple[0]) # 删除元组中的元素, 会报错

# 元组中常用的方法
# count() 返回元素的数量
print(my_tuple.count(1))
# index() 返回元素的索引
print(my_tuple.index(1))
# 元组的连接
print(my_tuple + my_tuple1)
# 元组的重复
print(my_tuple * 2)
# 元组的成员资格
print(1 in my_tuple)
print(6 in my_tuple)
print(1 not in my_tuple)
# 元组的排序
# sorted() 返回排序后的元组
print(sorted(my_tuple))  # 返回的是列表
# 元组的反转
# reversed() 返回反转后的元组
print(list(reversed(my_tuple)))  # 返回的是列表
# 元组的连接
# join() 将序列中的元素连接成字符串
# print("".join(my_tuple)) # 会报错

# 元组的遍历
for item in my_tuple:
    print(item)
# 使用枚举遍历
for index, item in enumerate(my_tuple):
    print(index, item)
# range() 遍历
for index in range(len(my_tuple)):
    print(index, my_tuple[index])
# 元组的嵌套
my_nested_tuple = (1, 2, (3, 4, 5), 6)
print(my_nested_tuple)
# 元组的嵌套访问
print(my_nested_tuple[2][0])
