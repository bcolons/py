import threading
import sys
import asyncio
def read1(fd,fdt):
    '(blocking) read(1) from passed fd, call writeall to spam all ttys'
    char=fd.read(1)
    if(char == 'q'):
        return 0
    writeall(fdt, fd.name+' '+char*int(char)+'\n')
    read1(fd,fdt)
def writeall(fdt,string):
    'spam-write any input char to all ttys in fdt arr'
    for fd in fdt:
        fd.write(string)
        fd.flush()
async def main():
    '''Enter a digit from either tty2/3, char is spammed that many times to both ttys. Basis for a char-level group chat server. Non-blocking doesnt prevent missed char reads(sadly).... open read and write file descriptors for ttys 2, 3. FIXME: close these fds.. .
    '''
    fdt=[]
    fdt+=open('/dev/tty2','w')
    fdt+=open('/dev/tty3','w')
    await asyncio.gather(
        asyncio.to_thread(read1,open('/dev/tty3','r') ,fdt),
        asyncio.to_thread(read1,open('/dev/tty3','r') ,fdt))
    print('I run...after until a q is entered in each tty')
    for each in threading.enumerate():
        print(each)
asyncio.run(main())
