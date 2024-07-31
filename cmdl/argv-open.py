import sys
import os
import time
'Simple example to write bytes from argv[1] file to argv[2] (which might be /dev/tty2, some other shells stdin)'
with open(sys.argv[1],'r') as fd:
    with open(sys.argv[2],'w') as fdo:
        while True:
            o=fd.read(1) # this guy is happy getting zero bytes back and returning
            time.sleep(1)
            num=fdo.write(o)
            time.sleep(1)
            print(num)
