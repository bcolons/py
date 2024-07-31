import subprocess
import sys
import os
'''Generate a file list with a cmd and apply a sequence of other cmds, appending output on a line
    Invoke as: cmd1 | python supscal.py cmd2 cmd3 cmd4 
    Note that cmd1 doesnt ever need to complete (although there may be a buffer overflow _bc)
    Other use cases: 
        cmd 'arbitrary text with $input_file_name' ie. cp $file $file.old
        cmd 'arbitrary text' ie. regex s/old/new
'''
    
    
while True:
    inp=None
    out=''
    outn=''
    outfw=open('/tmp/tempf','w')
    outfr=open('/tmp/tempf','r')
    inp=sys.stdin.readline()  # stdin-block and read until\n
    if(not inp): break
    inp.strip('\n')
    for each in sys.argv[1:]:
        subprocess.call(each+' '+inp,shell=True,stdout=outfw) # dont know how to do wo a file
        outn=outfr.readline()
        out+=outn.strip('\n')
    print(out)    
    outfw.close()
    outfr.close()
    # subprocess.call('rm /tmp/tempf',shell=True)  doesnt work_bc
