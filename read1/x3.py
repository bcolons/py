import subprocess
import sys

with subprocess.Popen('bc',stdin=subprocess.PIPE) as comproc:
    #with subprocess.Popen('bc') as comproc: # dumps execution into interactive (in this case) subprocess 
    comproc.stdin.write(b'3+9\n')
    comproc.stdin.write(b'32+9\n')
