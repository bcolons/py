import subprocess
import sys
import os
import re
'''Rename each filename from stdin with its correct file type suffix
    Invoke as: cmd1 | python rename.py
'''
typesuffd={
    re.compile('[mM][pP]') : 'mp4'
    re.compile('[eE][bB][mM]') : 'webm'
    re.compile('[eE][bB][pP]') : 'webp'
    re.compile('[zZ][iI][pP]') : 'gz'
    re.compile('ASCII') : 'txt'
    re.compile('[zZ][iI][pP]') : 'gz'
    }
    
suff=re.compile('\..*')
def suff(inpf):
    return suff.search(inpf)
    
while True:
    inp=None
    out=''
    outfw=open('/tmp/tempf','w')
    outfr=open('/tmp/tempf','r')
    inp=sys.stdin.readline()  # stdin-block and read until\n
    if(not inp): break
    inp.strip('\n')
    subprocess.call('file '+inp,shell=True,stdout=outfw) # dont know how to do wo a file
    out=outfr.readline()
    if(None == suff(out)):
        for each in typesuffd:
            is_match= each.match(out)):
            if(None != is_match(out)):
                subprocess.call('mv inp inp'+is_match.match,shell=True)
    outfw.close()
    outfr.close()
    # subprocess.call('rm /tmp/tempf',shell=True)  doesnt work_bc
