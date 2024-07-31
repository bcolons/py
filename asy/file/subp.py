import asyncio 
import time as t

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    print('l;asdfasdfqwert')
    await asyncio.sleep(2)
    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')
while True:
    i=input(str(t.time())+'tener comd: ')
    asyncio.run(run(i))
