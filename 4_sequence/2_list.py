# 列表
# 列表是 Python 中的一种数据类型，是有序排列的可变的元素集合，可以通过索引访问。
# 列表中的元素是不同类型的
# 列表中每个元素都是有对应位置的，称为索引或者下标，索引从0开始向后逐个递增
# 列表的创建
my_list = [1, 2, 3, 4, 5, 2, 2]
print(my_list)
# 列表的创建, 可以将其他的序列转换为列表
my_list1 = list()
print(my_list1)
# 列表的访问
print(my_list[0])
print(my_list[1])
print(my_list[2])
# 列表的切片
print(my_list[1:3])
# 列表的迭代
for item in my_list:
    print(item)
for i, var in enumerate(my_list):
    print(f"enumerate: {i} - {var}")
# 列表的长度
print(len(my_list))
# 列表的添加
my_list.append(6)
print(my_list)
# 列表的删除
my_list.remove(2)
print(my_list)
# 列表的修改
my_list[0] = 10
print(my_list)

# 通过切片修改
my_list1 = [10, 20, 30, 30]
my_list1[1:2] = [21, 31]
print(f"my_list1: {my_list1}")

# 方法
# append() 在列表的末尾添加元素
my_list.append(6)
print(my_list)
# extend() 在列表的末尾添加另一个列表
my_list.extend([7, 8])
print(my_list)
# insert() 在指定位置插入元素
my_list.insert(0, 0)
print(my_list)
# remove() 删除第一次出现的指定元素
my_list.remove(2)
print(my_list)
# pop() 删除指定位置的元素
my_list.pop(0)
print(my_list)

# index() 返回指定元素的索引
my_list = [1, 2, 3, 4, 5]
print(my_list.index(3))
# count() 返回指定元素的数量
print(my_list.count(3))

# sum(my_list) 返回列表中所有元素的和
print(sum(my_list))

# clear() 清空列表
my_list.clear()
print(my_list)

# 删除list
del_test = ["q", "w", "e"]
# 根据index删除其中某个元素
del del_test[0]
print("del_list:", del_test)

# 删除其中几个元素
del del_test[0:2]
print("del_test:", del_test)

# 删除整个列表
del del_test

# 列表推倒式,在已存在的课迭代对象基础上，通过运算或过滤，得到新的列表
list2 = [i * 2 for i in range(5)]
print(f"list2: {list2}")
list3 = [i * 2 for i in range(10) if i % 2 == 0]
print(f"list3: {list3}")
# 包含多个循环的列表推导式
list3 = [1, 2, 3, 4]
list4 = [5, 6, 7, 8]
list5 = [(i, j) for i in list3 for j in list4]
print(f"list5: {list5}")

# zip拉链函数
list6 = [1, 2, 3]
list7 = [4, 5, 6, 7]
zipped = zip(list6, list7)
print(f"zipped: {zipped}")
# 迭代zip对象
# for item in zipped:
#     print(item)
# 将zip转换成列表
list8 = list(zipped)
print(f"list8: {list8}")
