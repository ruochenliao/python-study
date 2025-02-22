"""
元组（Tuple）和Java中的数组（Array）有一些相似之处，但也有一些重要的区别。

相似之处：
元组和数组都是用于存储多个值的数据结构。
元组和数组都可以通过索引访问其元素。
元组和数组都可以包含不同类型的元素。

不同之处：
元组是不可变的（immutable），一旦创建就不能修改。而数组是可变的，可以通过索引修改其元素的值。
元组使用圆括号 () 来表示，而数组使用方括号 [] 来表示。
元组可以包含任意数量的元素，而数组在创建时需要指定固定的长度。
元组可以包含不同类型的元素，而数组通常包含相同类型的元素。

"""

# 打印第2个元素以后的
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2:])

# returns the items from index -4 (included) to index -1 (excluded)
print(my_tuple[-4:-1])

if 3 in my_tuple:
    print("3 is in the tuple")

# 将元组转换为列表
my_list = list(my_tuple)
print(my_list)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)