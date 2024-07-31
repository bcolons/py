import threading
'read and print  one character from /dev/tty2 once it becomes available, via five threads to maximize listen-uptime and minimize missed characters.' 
def read1(tty):
    with open(tty,'r') as fd: 
        while True:
            char=fd.read(1) # blocks if no chars read
            if char != '\n':
                print(char)
thread1=threading.Thread(target=read1,args=('/dev/tty2',))
thread2=threading.Thread(target=read1,args=('/dev/tty2',))
thread3=threading.Thread(target=read1,args=('/dev/tty2',))
thread4=threading.Thread(target=read1,args=('/dev/tty2',))
thread5=threading.Thread(target=read1,args=('/dev/tty2',))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
