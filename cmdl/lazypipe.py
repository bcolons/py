import sys
import os
'''Program executes: input_pipe_files|cmd $each_file. eg. ls|python lazypipe.py wc
    Invoke as: cmd1 | python lazypipe.py cmd2 (file_elem_from_cmd1_output_list)
    Note that cmd1 doesnt ever need to complete (although there may be a buffer overflow _bc)
    Other use cases: 
    cmd 'arbitrary text with $input_file_name' ie. cp $file $file.old
    cmd 'arbitrary text' ie. regex s/old/new
'''
    
    
while True:
    inp=None
    inp=sys.stdin.readline()  # stdin-block and read until\n
    if(not inp): break
    os.system(sys.argv[1]+' '+ inp.strip("\n"))
