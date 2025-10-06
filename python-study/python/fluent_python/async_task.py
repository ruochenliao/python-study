import asyncio
import time

def synchronous_task():
    """一个耗时的同步任务"""
    time.sleep(3)  # 模拟耗时操作
    return "同步任务完成"

async def async_task():
    """异步任务"""
    print("开始异步任务")
    # 错误做法：直接调用同步方法会阻塞事件循环
    result = synchronous_task()  # 这会导致事件循环被阻塞3秒
    print(result)
    return result

async def other_async_task():
    """另一个异步任务"""
    for i in range(5):
        print(f"其他任务正在运行 {i}")
        await asyncio.sleep(0.5)

async def main():
    # 同时运行两个异步任务
    task1 = asyncio.create_task(async_task())
    task2 = asyncio.create_task(other_async_task())
    await asyncio.gather(task1, task2)

asyncio.run(main())

# 在上面的例子中，other_async_task应该每0.5秒输出一次，但由于 synchronous_task的阻塞，它会等到3秒后才一次性输出所有内容。
import asyncio
import time

def synchronous_task():
    """一个耗时的同步任务"""
    time.sleep(3)
    return "同步任务完成"

async def async_task():
    """异步任务"""
    print("开始异步任务")
    # 正确做法：使用 to_thread 在后台线程中运行同步函数
    result = await asyncio.to_thread(synchronous_task)
    print(result)
    return result

async def other_async_task():
    """另一个异步任务"""
    for i in range(5):
        print(f"其他任务正在运行 {i}")
        await asyncio.sleep(0.5)

async def main():
    task1 = asyncio.create_task(async_task())
    task2 = asyncio.create_task(other_async_task())
    await asyncio.gather(task1, task2)

asyncio.run(main())
