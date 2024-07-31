import subprocess
proc = subprocess.Popen('ls',stdout=subprocess.PIPE)
print('higuy')
print(proc.stdout) #nothing here, yet
print('biguy')
proc2= subprocess.Popen(['python','tr.py'],stdin=proc.stdout)
print(proc2.stdout)
