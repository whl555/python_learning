import asyncio
# from lib import timer # ModuleNotFoundError: No module named 'lib'
from lib import timer # ImportError: attempted relative import with no known parent package

async def print_odd(even_event, odd_event):
    num = 1
    while num <= 100:
        await odd_event.wait()  # 等待奇数事件触发
        print(f"奇数: {num}")
        num += 2
        odd_event.clear()       # 重置奇数事件
        even_event.set()        # 触发偶数事件

async def print_even(even_event, odd_event):
    num = 0
    even_event.set()            # 初始触发偶数协程
    while num <= 100:
        await even_event.wait() # 等待偶数事件触发
        print(f"偶数: {num}")
        num += 2
        even_event.clear()      # 重置偶数事件
        if num <= 100:
            odd_event.set()     # 触发奇数事件

@timer
async def main():
    even_event = asyncio.Event()
    odd_event = asyncio.Event()
    await asyncio.gather(
        print_even(even_event, odd_event),
        print_odd(even_event, odd_event)
    )

asyncio.run(main())

def test():
    asyncio.run(main())
