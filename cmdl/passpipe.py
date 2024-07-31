import sys
'''Example of program which uses input pipe or interactive stdin and returns each line until EOF.
    Usage: python passpipe.py <file1
    ...to read, print each line of file1, halt on EOF'''
inp=''
while True:
    inp=sys.stdin.readline()  # inp is 0 on read(EOF)
    #inp=sys.stdin.read(2)  # stdin-block once 2 chars read return, stdin is buffered
    if(not inp): break
    print(inp)
