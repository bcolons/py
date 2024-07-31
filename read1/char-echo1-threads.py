import threading
#import tty
'''read and print single characters to-and-from /dev/tty2 from-and-to tty3 via threads.
'''
def echo1(ttyi,ttyo):
    with open(ttyi,'r') as fdi: 
        with open(ttyo,'w') as fdo: 
            #tty.setraw(fdi) # unbufferd ...no effect
            #tty.setraw(fdo) # unbuffered ...no effect
            while True:
                char=fdi.read(1) # blocks if no chars read
                num=ord(char)-ord('a')+1 # char printed ordinal number of times plus newline
                fdo.write(char*num+'\n')
                fdo.flush()
thread1=threading.Thread(target=echo1,args=('/dev/tty2','/dev/tty3'))
thread2=threading.Thread(target=echo1,args=('/dev/tty3','/dev/tty2'))
thread1.start()
thread2.start()
