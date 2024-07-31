import subprocess
import sys
args=[]
args.append(sys.argv[1])
for each in sys.argv[2:]:
    args.append(each)
proc=subprocess.Popen(args)#,stdin=subprocess.PIPE)
stdin=proc.stdin
print(stdin)
