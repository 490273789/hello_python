import asyncio


async def greet(name, s):
    await asyncio.sleep(s)
    return name
# 运行单个协程或者任务
async def main():
    try:
        result = await asyncio.wait_for(greet("www", 2))
        print(result)
    except asyncio.Timeout:
        print("超时了")
        
        
if __name__ == "__main__":
    asyncio.run(main())