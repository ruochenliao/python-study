# 表示地理位置的经纬度
class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

moscow = Coordinate(55.76, 37.62)
location = Coordinate(55.76, 37.62)
print(location == moscow)
print((location.lat, location.lon) == (moscow.lat, moscow.lon))

moscow = Coordinate(55.76, 37.62)
print(moscow == Coordinate(lat=55.76, lon=37.62))


from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


# 普通的类申明
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

p = Person(name="nebula", age= 100)
print(p)


# 使用NamedTuple, 不可变（创建后不能修改字段值）
from typing import NamedTuple
class Person(NamedTuple):
    name: str
    age: int
p = Person(name="nebula", age= 100)
print(p)

from dataclasses import dataclass

# 可变（默认），但可通过 @dataclass(frozen=True)设为不可变。
@dataclass
class Person:
    name: str
    age: int

p = Person(name="nebula", age= 100)
print(p)
p.age = 101
print(p)

# 定义ClubMember
from dataclasses import dataclass, field

@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)

c = ClubMember(name="nebula")
print(c)

from dataclasses import dataclass, field, fields
from typing import Optional
from enum import Enum, auto
from datetime import date


class ResourceType(Enum):  # <1>
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()


@dataclass
class Resource:
    """描述媒体资源"""
    identifier: str
    title: str = '<untitled>'
    creators: list[str] = field(default_factory=list)
    date: Optional[date] = None
    type: ResourceType = ResourceType.BOOK
    description: str = ''
    language: str = ''
    subjects: list[str] = field(default_factory=list)

    def __repr__(self):
        cls = self.__class__
        cls_name = cls.__name__
        indent = ' ' * 4
        res = [f'{cls_name}(']
        for f in fields(cls):
            value = getattr(self, f.name)
            res.append(f'{indent}{f.name} = {value!r},')

        res.append(')')
        return '\n'.join(res)

description = 'Improving the design of existing code'
book = Resource('978-0-13-475759-9', 'Refactoring, 2nd Edition',
                ['Martin Fowler', 'Kent Beck'], date(2018, 11, 19),
                ResourceType.BOOK, description, 'EN',
                ['computer programming', 'OOP'])

print(book)

