import sys
import time
'''
    Blocking read byte, write-and-flush byte from stdin to /dev/tty2
    Exit when read(EOF)
'''
with open('/dev/tty2','w') as fdo:
    while True:
        o=sys.stdin.read(1)
        time.sleep(1)
        if(o):
            fdo.write(o)
            fdo.flush()
        else: break # Ctrl-d or EOF
        
        
