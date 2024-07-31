import sys
import os
'''Generic pattern for accepting a list of files as args or listed on lines of stdin.
Here files are read from lines of stdin then commandline filenames are applied
First argument is command to apply to each file. _bc not done...
'''
def parse_stdin(stdin):
    inp=sys.stdin.readline()
    if(inp): 
        print('parsed: '+inp)
        yield inp.strip('\n')

def invoke(stdin, cmd, *files):
    inps=parse_stdin(stdin)
    for each in inps:
        os.system(cmd+' '+each)
    for each in files:
        print(each)
        os.system(cmd+' '+each)
    
print(sys.stdin,'argv',str(sys.argv)+'\n')
invoke(sys.stdin,sys.argv[1],sys.argv[2:])
