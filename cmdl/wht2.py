import sys
'''Example of program which uses input pipe or interactive stdin and returns bytes or lines.'''
while True:
    inp=[]
    inp=sys.stdin.readline()  # stdin-block and read until\n
    #inp=sys.stdin.read(2)  # stdin-block once 2 chars read return, stdin is buffered
    print(f'isatty: {sys.stdin.isatty()}')# input pipe for example
    print(f'linebuffering: {sys.stdin.line_buffering}') #readonly according to runtime
    print(inp)
