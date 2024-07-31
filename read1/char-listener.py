import threading
import tty
'''read and print one character from /dev/tty2 via a thread.
'''
def read1(tty_):
    with open(tty_,'r') as fd: 
        tty.setraw(fd) # unbuffered 
        while True:
            char=fd.read(1) # blocks if no chars read
thread1=threading.Thread(target=read1,args=('/dev/tty2',)) # note that more threads dont free up GIL, nor impact missed chars
thread1.start()
