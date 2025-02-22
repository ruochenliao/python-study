"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
print(len(my_list))
print(type(my_list))
# 打印第5个
print(my_list[5])

# 打印第0到第5个
print(my_list[0:5])

# 打印第0到第10个，步长为2
print(my_list[0:10:2])

# 打印最后一个
print(my_list[-1])

# 把200插入到第3个位置
my_list.insert(2, 200)
print(my_list)

# 删除200
my_list.remove(200)
print(my_list)

# 添加一个元素
my_list.append(11)
print(my_list)

# 删除最后一个
my_list.pop()
print(my_list)

# 添加一个列表
my_list.extend([12, 13, 14])
print(my_list)

# 删除第12个
del my_list[12]
del my_list[11]
del my_list[10]
print(my_list)

# 清空
my_list.clear()
print(my_list)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list.sort(reverse=True)
print(my_list)

my_list.sort()
print(my_list)

new_list = my_list.copy()
print(new_list)
new_list = list(my_list)
print(new_list)

# 从第3个到第4个切片
my_slice = my_list[3:4]
print(my_slice)

# 拼接2个
my_list = [1, 2, 3, 4, 5] + [6, 7, 8, 9, 10]
print(f"拼接{my_list}")

# 拼接2个完全不同的列表
my_list = [1, 2, 3, 4, 5] + ["a", "b", "c", "d", "e"]
print(my_list)