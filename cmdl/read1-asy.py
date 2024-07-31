#doesnt work
import asyncio
'''while True: read and print (via a callback) one character from /dev/tty2 once available in the add_reader sense (right away)'''
def read1(fd):
    char=fd.read(1)
    fd.flush()
    if char != '\n':
        print(char)
async def main():
    loop=asyncio.get_running_loop()
    while True:
        with open('/dev/tty2','r') as tty2:
            loop.add_reader(tty2,read1(tty2))
asyncio.run(main())
