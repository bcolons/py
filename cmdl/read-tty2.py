import sys
#import os
import time
'''Simple example to write bytes from stdin to /dev/tty2 (some other shells stdin)
    Demo for sys.stdout.flush() which pushes output buffer for o/w non-blocking writes
    _bc Downstream pipes manage their own buffer....
'''
with open('/dev/tty2','w') as fdw:
    while True:
        o=sys.stdin.read(1) # this guy is happy getting zero bytes back and returning 
        if(o):
            #fdw.write('incoming...\n') # where fdo is /dev/tty2 only full lines appear at a time, why? 
            #input buffer is a char[], lines are elements with terminating \n? 
            num=fdw.write(o) # where fdo is /dev/tty2 only full lines appear at a time, why? 
            time.sleep(1)
            time.sleep(1)
            num=fdw.write(o) # where fdo is /dev/tty2 only full lines appear at a time, why? 
            fdw.flush() # above writes show up simultaneously 
            sys.stdout.write(f'{o}') #print('written to argv[1]: '+o)
            sys.stdout.flush()
        else: break
