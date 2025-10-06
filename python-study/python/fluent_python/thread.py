import asyncio

# 定义一个异步函数
async def say_after(delay, what):
    # 1. 使用 await 等待一个“可等待对象”（Awaitable）
    # 2. asyncio.sleep() 是一个异步的等待函数，模拟I/O操作
    await asyncio.sleep(delay)
    print(what)

# 调用异步函数
coro = asyncio.run(say_after(1, 'Hello world!')) # 这仅仅创建了一个协程对象，代码并未执行
print(coro) # 输出: <coroutine object say_after at 0x...>

