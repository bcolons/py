import threading
import sys
'Enter a digit from either tty2/3, char is spammed that many times to both ttys. Basis for a char-level group chat server. Blocking means char are not read....'
def read1(fd,fdt):
    'blocks a thread on a tty until a char is typed'
    char=fd.read(1)
    writeall(fdt, fd.name+' '+char*int(char)+'\n')
    read1(fd,fdt)
def writeall(fdt,string):
    'spams/writes a string to an arr of ttys'
    for fd in fdt:
        fd.write(string)
        fd.flush()

fdt=[] # arr of tty's for spam writing
fdt+=open('/dev/tty2','w')
fdt+=open('/dev/tty3','w')

print('before... '+str(threading.active_count()))
threading.Thread(target=read1,args=(open('/dev/tty3','r'),fdt)).start()
threading.Thread(target=read1,args=(open('/dev/tty2','r'),fdt)).start()
print('after... '+str(threading.active_count()))
for each in threading.enumerate():
    print(each)
