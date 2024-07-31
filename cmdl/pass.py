import sys
'''Generic pattern for lazy or line-streaming from stdin.
'''
def lazy_parse_fd(fd,token='\n'):
    '''Generating parser. Reads a file descr; yields data btwn tokens; exits on EOF'''
    inp=True
    line=''
    while(inp): #loop exits on read(1)=='' or EOF
        inp=fd.read(1)
        if(inp != token): line+=inp
        else: 
            yield line
            line=''

def invoke(fdi,cmd,fdo):
    '''Call cmd on lines of input, writing output after each.'''
    inps=lazy_parse_fd(fdi)
    for each in inps: 
        subcommand.call(cmd+' '+each,shell=True,stdout=fdo)
        sys.stdout.write(fdo.read
        sys.stdout.flush()
        
    
invoke(sys.stdin,sys.argv[1],sys.stdout)
