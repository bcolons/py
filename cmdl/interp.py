import sys
import os
'''Program allows a user to type text, \n terminating lines are sent to stdout for use with a sbsq pipe.
'''
    
    
while True:
    inparr=''
    inp=''
    inp=sys.stdin.read(1)  # stdin-block and read until\n
    inparr+=inp
    if(inp == '\n'):
        sys.stdout.write(inparr)
        sys.stdout.flush()
        inparr=''
    if(inp == ''):
        break
