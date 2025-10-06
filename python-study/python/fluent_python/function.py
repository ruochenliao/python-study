# 函数可以被赋值给变量
def greet(name):
    return f"Hello, {name}!"

# 将函数赋值给变量
say_hello = greet
print(say_hello("Alice"))  # 输出: Hello, Alice!

# 函数可以作为参数传递给其他函数
def apply(func, value):
    return func(value)

def square(x):
    return x * x

print(apply(square, 5))  # 输出: 25
print(apply(str.upper, "hello"))  # 输出: HELLO

# 函数可以作为返回值
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 输出: 10
print(triple(5))  # 输出: 15

# 函数可以存储在数据结构中
operations = {
    'add': lambda a, b: a + b,
    'subtract': lambda a, b: a - b,
    'multiply': lambda a, b: a * b
}

print(operations['add'](10, 5))      # 输出: 15
print(operations['multiply'](10, 5)) # 输出: 50

# 函数可以拥有属性
def counter():
    counter.count += 1
    return counter.count

counter.count = 0  # 给函数添加属性

print(counter())  # 输出: 1
print(counter())  # 输出: 2
print(counter.count)  # 输出: 2

# 回调函数
def process_data(data, callback):
    # 处理数据...
    result = data.upper()
    # 调用回调函数
    callback(result)

def print_result(result):
    print(f"处理结果: {result}")

process_data("hello", print_result)
# 输出: 处理结果: HELLO

# 装饰器
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数 {func.__name__} 执行完毕")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(3, 5))
# 输出:
# 调用函数: add
# 函数 add 执行完毕
# 8

# 闭包
def make_power(n):
    def power(x):
        return x ** n
    return power

square = make_power(2)
cube = make_power(3)

print(square(4))  # 输出: 16
print(cube(3))    # 输出: 27

# 高阶函数
# map() 函数
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出: [1, 4, 9, 16]

# filter() 函数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出: [2, 4]

# 函数对象有一些内置属性：
def example(a, b=1):
    """示例函数"""
    return a + b

print(example.__name__)    # 输出: 'example'
print(example.__doc__)     # 输出: '示例函数'
print(example.__module__)  # 输出: '__main__'
print(example.__defaults__) # 输出: (1,)
print(example.__code__.co_varnames) # 输出: ('a', 'b')

# 闭包（Closure）是指一个函数与其相关的引用环境（变量）的组合体​​。更具体地说
# 闭包是一个内部函数
# 该内部函数访问了外部函数（封闭函数）的变量
# 即使外部函数已经执行完毕，内部函数仍然"记住"并可以访问那些外部变量
# 闭包的三要素
# 一个闭包的形成需要三个关键要素：
# 嵌套函数：一个函数（外部函数）内部定义了另一个函数（内部函数）
# 变量引用：内部函数引用了外部函数的变量（称为自由变量）
# 返回内部函数：外部函数返回内部函数（作为返回值）
def outer_function(x):  # 外部函数
    def inner_function(y):  # 内部函数
        return x + y  # 引用了外部函数的变量x

    return inner_function  # 返回内部函数（不调用）


# 创建闭包
closure = outer_function(10)

# 使用闭包
print(closure(5))  # 输出: 15
print(closure(3))  # 输出: 13

# 闭包的特殊行为
# 闭包的神奇之处在于它能"记住"外部环境的状态：
def counter():
    count = 0  # 外部函数的变量

    def increment():
        nonlocal count  # 声明使用外部变量
        count += 1
        return count

    return increment


# 创建两个独立的计数器
counter1 = counter()
counter2 = counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1 (独立的计数)
print(counter1())  # 3

# 每次调用 counter()都会创建一个新的闭包实例
# 每个闭包都有自己的 count变量副本
# 闭包保持了状态（计数）而不需要使用全局变量