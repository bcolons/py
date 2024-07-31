import asyncio
import sys
import time
import subprocess
import threading
import re

'Uses thread to unblock a normal blocking read(1), recursing to await sbsq char. There are two threads, an I/O tty and the main tty. FIXME: Second chars are sometimes missed...(multiple listeners would help)' 
def read1(fd,fdo):
    char=fd.read(1)
    if(char=='q'):
            fdo.write('quit!')
            fdo.flush()
            return -1 # exit the calling thread and drop out of main()
    elif(char=='x'):
            fdo.write('explain!')
            fdo.flush()
    elif(char=='h'):
            fdo.write('q- quit\nh h - help\n x -explain')
            fdo.flush()
            d=dir('character-interacter-thread')
            for each in d:
                fdo.write(each)
                fdo.write('\t')
                fdo.flush()
            stdo=subprocess.run(['grep','def.*(.*):',sys.argv[0]],capture_output=True) 
            n= re.split(r'\\n',str(stdo)   ) # need r'\\n' to split on the \n chars from preceding line
            for each in n:
                fdo.write('\n')
                fdo.write(each)
                fdo.write('\n')
                fdo.flush()
    else:
            fdo.write('nothing...')
            fdo.flush()
    read1(fd,fdo)

def main():
    try: # usage advice and exit if no commandline arg for another tty is given
        wreader=sys.argv[1]
    except IndexError:
        print('usage: \n python char-interacter-thread.py /dev/tty2 \n( or some alternate tty for character input and output)')
        return -1
    else:
        with open(wreader,'r') as fd: 
            with open(wreader,'w') as fdo: 
                threading.Thread(read1(fd,fdo)) # our listener, doesnt return until 'q' entered
main()

