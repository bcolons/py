import sys
#import os
import time
'Simple example to write bytes from argv[1] file to argv[2] (which might be /dev/tty2, some other shells stdin)'
with open('/dev/tty2','w') as fdw:
    while True:
        o=sys.stdin.read(1) 
        time.sleep(1)
        fdw.write('\nincoming...\n') # where fdo is /dev/tty2 only full lines appear at a time, why
        num=fdw.write(o) # where fdo is /dev/tty2 only full lines appear at a time, why
        #fdw.flush() # dont need this guy...single char writes go straight through
        time.sleep(1)
        print('written to argv[1]: '+o)
