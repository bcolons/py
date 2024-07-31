import asyncio
'''read and print single characters to-and-from /dev/tty2 from-and-to tty3 via threads.
'''
async def main():
    with open('/dev/tty2','r') as fdi2: 
        with open('/dev/tty2','w') as fdo2: 
            with open('/dev/tty3','w') as fdo3: 
                with open('/dev/tty3','r') as fdi3: 
                    L=await asyncio.gather(readwrite1(fdi2,fdo3),readwrite1(fdi3,fdo2)) #only goes one way,need a callback impl
async def readwrite1(fdi,fdo):
    while True:
        await asyncio.sleep(0)
        char=fdi.read(1) # blocks if no chars ead
        num=ord(char)-ord('a')+1 # char printed ordinal number of times plus newline
        fdo.write(char*num+'\n')
        fdo.flush()
asyncio.run(main())


