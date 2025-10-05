dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]
# 对调键和值
country_dial = {country: code for code, country in dial_codes}
country_dial

# 按国家名称排序，再次对调键和值，把值转成大写，筛选code<70的项
result = {code: country.upper()
    for country, code in sorted(country_dial.items())
    if code < 70}
print(result)

def dump(**kwargs):
    return kwargs

result = dump(**{'x' :1}, y=2, **{'z': 3})
print(result)

d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
d = d1 | d2
print(d)


def get_match(key):
    match key:
        case 'a':
            return 'A'
        case 'b':
            return 'B'
        case _:
            return '?'

print(get_match('a'))
print(get_match('c'))

def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            return ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            return ValueError(f'Invalid record: {record!r}')

print(get_creators({'type': 'book', 'api': 1, 'author': 'Alice'}))


