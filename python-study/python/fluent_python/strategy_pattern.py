# 注册中心：一个空列表，将来所有被装饰的策略函数都会在这里
registered_strategies = []

# 注册器（装饰器）
def register_strategy(func):
    """
    这个装饰器将策略函数 `func` 添加到 `registered_strategies` 列表中。
    """
    registered_strategies.append(func) # 核心操作：自动注册
    return func # 返回原函数，不影响其本身的行为

@register_strategy
def upper_case(text: str) -> str:
    """策略1：全部大写"""
    return text.upper()

@register_strategies
def lower_case(text: str) -> str:
    """策略2：全部小写"""
    return text.lower()

@register_strategy
def capitalize_case(text: str) -> str:
    """策略3：首字母大写"""
    return text.capitalize()

# 假设我们后来又想加一个新策略，非常简单！
@register_strategy
def reverse_text(text: str) -> str:
    """（新增）策略4：反转文本"""
    return text[::-1]

def process_text(text: str, strategy_name: str) -> str:
    """
    根据策略名称处理文本。
    """
    # 在注册中心里查找策略
    for strategy in registered_strategies:
        if strategy.__name__ == strategy_name:
            # 找到后直接调用这个函数
            return strategy(text)
    raise ValueError(f"Unknown strategy: {strategy_name}")

# 更强大的用法：自动应用所有策略
def apply_all_strategies(text: str) -> dict:
    """应用所有注册的策略，并返回结果字典。"""
    results = {}
    for strategy in registered_strategies:
        results[strategy.__name__] = strategy(text)
    return results

# 1. 使用特定策略
input_text = "Hello, World!"
print(process_text(input_text, 'upper_case'))
# 输出: HELLO, WORLD!

# 2. 动态展示所有策略的效果
all_results = apply_all_strategies(input_text)
print(all_results)
# 输出:
# {
#   'upper_case': 'HELLO, WORLD!',
#   'lower_case': 'hello, world!',
#   'capitalize_case': 'Hello, world!',
#   'reverse_text': '!dlroW ,olleH'
# }
