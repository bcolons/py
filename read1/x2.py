import subprocess
import sys

args=[]
args.append(sys.argv[1])
for each in sys.stdin:
    print('cur:'+each)
    comproc=subprocess.run(str(args)+' '+each)
