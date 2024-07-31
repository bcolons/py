import asyncio
async def myawaiter():
    await asyncio.sleep(1)
asyncio.run(myawaiter())
