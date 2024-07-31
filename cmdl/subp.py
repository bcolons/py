import subprocess
import sys
#subprocess.call(['ls','-l','a*']) # shell=None ....no shell wildcard avail
#subprocess.call(['ls','-l','w*'],shell=True)
with open('tmpfil','r') as tfdo:    
    with open('tmpfil','w') as tfdi:
        while True:
            #subprocess.call(['wc']) #happily invoked on zero input read from stdin,must manual managed instd
            #need to pull as many bytes as can until '', execute, repeat...
            inp=sys.stdin.readline()
            tfdi.write(inp)
            tfdi.flush()
            if(inp):
                subprocess.call(['wc'],stdin=tfdo) # writes once... nevers exits?
                print('we returne!')
