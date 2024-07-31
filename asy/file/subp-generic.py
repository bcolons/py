import asyncio
import sys

async def get_date():
    '''Single-coro, busy-system-friendly sub-process example. 
    Each 'await' occurs in sequence unlike asy.gather(..) and asy.(as_completed)'''
    code = 'import datetime; print(datetime.datetime.now())'

    # Create the subprocess; redirect the standard output
    # into a pipe  
    # (...create python subp and run 'code=...' with it 'await'-ing lazy assignment of a proc var ).
    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdout=asyncio.subprocess.PIPE)

    # Read (eg. 'await' one..) one line of output.
    data = await proc.stdout.readline()
    line = data.decode('ascii').rstrip()

    # Wait for the subprocess exit. (on its own...)
    await proc.wait()
    return line

date = asyncio.run(get_date())
print(f"Current date: {date}")
