def deco(func):
    def inner():
        print('running inner')
    return inner

@deco
def target():
    print('running target()')

target() # 输出 running inner


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