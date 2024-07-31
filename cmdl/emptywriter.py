import sys
import time
for ct in range(3):
    sys.stdout.write(f'hey{ct}\n')
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write(f'hooo{ct}\n')
    time.sleep(1)
    #sys.stdout.close() # system call, closes pipe just like Ctrl-d / EOF
sys.stdout.close() # system call, closes pipe just like Ctrl-d / EOF
    #i/o on closed Error: sys.stdout.write('wwhhhooo\n')
