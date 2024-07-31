import subprocess
import asyncio

print('hey')
cmd=['ls','-l']
def r(cmd):
    subprocess.run(cmd)
#exec('ls')
