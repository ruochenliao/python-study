# classmethod：定义操作类而不是操作实例的方法，常见用途是定义备选构造函数。
# staticmethod：静态方法，不是特别有用。
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 一个普通的实例方法，操作的是实例 (self)
    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old.")

    # 一个类方法，操作的是类 (cls)
    @classmethod
    def from_birth_year(cls, name, birth_year):
        # 注意参数是 cls，而不是 self
        # cls 代表 Person 这个类本身
        current_year = 2023
        age = current_year - birth_year
        # 这里等同于调用 Person(name, age)
        # 但用 cls 更通用，即使类名变了或者有继承也能正常工作
        return cls(name, age) # 调用类的构造方法并返回一个实例

# 使用标准的 __init__ 方法创建对象
p1 = Person("Alice", 25)
p1.introduce() # 输出: Hi, I'm Alice, 25 years old.

# 使用类方法作为“工厂函数”来创建对象
# 无需计算年龄，直接传入出生年份即可
p2 = Person.from_birth_year("Bob", 1995)
p2.introduce() # 输出: Hi, I'm Bob, 28 years old.
print(p2.age) # 输出: 28

# 操作或修改类状态
class Car:
    total_cars = 0 # 这是一个类属性

    def __init__(self, model):
        self.model = model
        # 当创建新实例时，通过类方法更新计数器
        self.increment_cars()

    @classmethod
    def increment_cars(cls):
        cls.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

car1 = Car("Tesla Model S")
car2 = Car("Toyota Camry")

print(Car.get_total_cars()) # 输出: 2 (调用类方法，操作类属性)

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# 无需创建 Calculator 实例，直接通过类调用
result = Calculator.add(5, 3)
print(result) # 输出: 8

result2 = Calculator.multiply(5, 3)
print(result2) # 输出: 15

class User:
    def __init__(self, username):
        self.username = username

    @staticmethod
    def is_valid_username(username):
        # 这是一个工具函数，检查用户名是否有效
        # 它不访问 self 或 cls，只操作自己的输入参数
        return len(username) >= 4 and username.isalnum()

# 在创建 User 实例前，可以先使用这个静态方法验证
if User.is_valid_username("Tom"):
    user = User("Tom")
    print("User created!")
else:
    print("Invalid username!")


from typing import Dict

# 一个表示用户信息的字典
user: Dict[str, object] = {
    'name': 'Alice',
    'age': 30,
    'is_active': True
}

# 类型检查器只知道这是一个 Dict[str, object]。
# 它无法知道：
# 1. 必须有 'name', 'age', 'is_active' 这些键。
# 2. 'name' 的值必须是 str，'age' 的值必须是 int。
# 因此，下面的错误代码不会被类型检查器捕获：
user['name'] = 123 # 把名字改成数字？类型检查器可能不会报错
user['email'] = 'alice@example.com' # 添加了一个未预期的键？也不会报错
print(user)

from typing import TypedDict

# 定义一个表示用户的 TypedDict
class User(TypedDict):
    name: str
    age: int
    is_active: bool
    # 你可以将某个键标记为可选（非必须）
    email: str | None # 使用 Union 类型 (Python 3.10+ 也可用 str | None)

# 现在使用它
user1: User = {
    'name': 'Alice',
    'age': 30,
    'is_active': True,
    # 'email' 是可选的，所以可以不提供
}
# 类型检查器会验证你的字典是否符合 User 的结构

# 访问键时，IDE 和类型检查器能推断出正确的类型
name: str = user1['name'] # IDE 知道 name 是 str 类型
age: int = user1['age']   # IDE 知道 age 是 int 类型

# 错误的赋值会被类型检查器（如mypy）捕获
user1['age'] = 'thirty' # 错误: 不能将 str 赋给 int 类型的键
user1['address'] = '123 Street' # 错误: User 中没有 'address' 键
print("result")
print(user1)