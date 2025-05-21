# 列表
# 列表是 Python 中的一种数据类型，成员是有序排列的，可以通过索引访问。
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
# remove() 删除指定元素
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
# 删除其中某个元素
del del_test[0]
print("del_list:", del_test)

# 删除其中几个元素
del del_test[0:2]
print("del_test:", del_test)

# 删除整个列表
del del_test
