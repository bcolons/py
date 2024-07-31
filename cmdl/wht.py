import sys
while True:
    inp=[] #sys.stdin.read()  # block and read until an  entered
    #inp=sys.stdin.read(1)  # block and read 1 char
    inp+=sys.stdin.readline()  # block until 2 chars read, returns ...stdin is buffered
    if(not inp): break # normal unix, EOF/CTRL-d terminates iter over \n delimited lines-of-input
    #sys.stdin.flush()   doesnt do anything ?
    print(f'isatty: {sys.stdin.isatty()}')
    print(f'linefuf: {sys.stdin.line_buffering}')
    sys.stdout.write(f'inp: {inp} ')
    sys.stdout.flush()
        
