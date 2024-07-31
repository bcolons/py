import sys
import subprocess
'''(Greedily and...) Immediately apply-and-eval a command given in argv1 to first line of stdin, lazy apply cmd to each sbsq line until EOF.
    1. read a line from stdin
    2. execute cmd in sys.argv[1] to line
    3. write entire output to stdout (right away)
    4. flush stdout 
    5. repeat to each line in stdin until EOF
'''
while True:
    o=sys.stdin.readline()
    print(f'o: {o}')
    if(o):
        subprocess.call([sys.argv[1],o.strip()],shell=True) #simplest case 'cmd arg1', stdin is EOF delimd buffer
    else: break
#subprocess.call([sys.argv[1]],shell=True)
#subprocess.call(['wc'],shell=True,stdin=sys.stdin)
#sys.stdout.flush()
#time.sleep(.1)
#else: break # Ctrl-d with empty buffer in shell 'EOF' ; comment-out for tail -f behavior
