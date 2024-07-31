import asyncio

background_tasks = set()

async def mycoro(i):
    print("f"+str(i))
    await asyncio.sleep(i)
    print("l"+str(i))

async def main():
    for i in range(10):
        task = asyncio.create_task(mycoro(i))
    
        # Add task to the set. This creates a strong reference.
        background_tasks.add(task)
    
        # To prevent keeping references to finished tasks forever,
        # make each task remove its own reference from the set after
        # completion:
        #task.add_done_callback(background_tasks.discard)
asyncio.run(main())
        
#template: async def f1(i): stuff, await asyncio.sleep(i), other not-done stuff
#template: async def f2(): task = asyncio.create_task(f2(123))
#template: asyncio.run(main())
