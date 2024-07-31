import sys
import time
''' Asynchronous processing of input to cmds joined via pipe.
    read-write-flush-a-line from stdin to stdout
    One Ctrl-d pushes interactive entries (also newline), a second pushes EOF (_bc somehow)
    Usage: <shell chars>|python rwf.py |python subproc.py cmd
    Lines of output show cmd <stdinput line>
'''
tee=sys.argv[1]
while True:
    o=sys.stdin.readline()
    if(tee): 
        with open('/dev/tty2','w') as tfdo:
            tfdo.write(f'{o}')
            tfdo.flush() # this is what is missing from 'normal' line-delim'd unix cmd output....
    if(o):
        sys.stdout.write(f'{o.strip()}')
        sys.stdout.flush() # this is what is missing from 'normal' line-delim'd unix cmd output....
        time.sleep(.5)
        #sys.stderr.write(f'E{o}') #too noisy for actual use pass the demo
        #sys.stderr.flush()
    else: 
        sys.stdin.close()
        sys.stdout.close()
        break # Ctrl-d with empty buffer in shell 'EOF' ; comment-out for tail -f behavior
    
