

import asyncio


async def greet(name, s):
    await asyncio.sleep(s)
    return name

async def main():
    aws = [
        greet('w', 1),
        greet('s', 3),
        greet('n', 2)
    ]
    
    # 可以指定超时时间，到时间了还没执行完，会抛出异常，执行完的任务不会被取消
    # 出现其他异常，剩余的任务也不会被取消
    for item in asyncio.as_completed(aws, timeout=4):
        print("------")
        result = await item
        print(result)
        
if __name__ == "__main__":
    asyncio.run(main())