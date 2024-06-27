import asyncio


async def hello():
    name = input('Enter your name: ') # Enter your name
    await asyncio.sleep(2) # wait for 2 seconds 
    print(f'hello {name}') # print hello to the name entered
asyncio.run(hello())