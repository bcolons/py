import sys
import time
''' Simplest demo to show asynchronous processing of cmds joined via pipe.
    read-write-flush-a-byte from stdin to stdout, delayed write to stderr
    One Ctrl-d pushes interactive entries (also newline), a second pushes EOF (_bc somehow)
    Usage: <shell chars>|python readwriteflush1.py |python readwriteflush1.py 
    Bytes will appear from second instance' stdout before first's stderr, QED (eg. b -> bEbEb)
'''
while True:
    o=sys.stdin.read(1)
    if(o):
        sys.stdout.write(f'{o}')
        sys.stdout.flush() # this is what is missing from 'normal' line-delim'd unix cmd output....
        time.sleep(.5)
        sys.stderr.write(f'E{o}')
        sys.stderr.flush()
    else: break # Ctrl-d with empty buffer in shell 'EOF' ; comment-out for tail -f behavior
    
