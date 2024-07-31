import subprocess
import sys

with subprocess.Popen(['bc','-l'],text=True,stdin=subprocess.PIPE) as comproc:
    #with subprocess.Popen('bc') as comproc: # dumps execution into interactive (in this case) subprocess 
    print(comproc.pid)
    comproc.communicate('2+2\n',timeout=99)
    if(comproc.poll()): #proc completes for some unk reason...
        print(comproc.communicate(input='2+2\n'))
    if(comproc.poll()):
        comproc.communicate(input='32+2\n')
    #comproc.stdin.write(b'32+9\n')
