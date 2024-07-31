import sys
#import os
import time
'Simple example to write bytes from stdin to /dev/tty2 (some other shells stdin)'
with open(sys.stdin) as fdr: #sys.stdin ...doesntwork
    with open('/dev/tty2','w') as fdw:
        while True:
            o=fdr.read(1) # this guy is happy getting zero bytes back and returning
            #time.sleep(1)
            fdw.write('incoming...sngle byte/char: '+o+' ') # where fdo is /dev/tty2 only full lines appear at a time, why? 
            num=fdw.write(o)
            fdw.flush() 
            time.sleep(1)
            print('written to tty2: '+o)
