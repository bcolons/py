import asyncio as a
async def uloop():
    while True:
        l=a.get_running_loop()
        i=input('write sumpin')
        print( await slowlen(i))
        
async def slowlen(s):
    await a.sleep(2)
    leng=len(s)
    await a.sleep(2)
    return leng
a.run(uloop())
