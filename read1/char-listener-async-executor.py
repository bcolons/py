import tty
import asyncio
import concurrent.futures

'''Code from 
    /mnt/c/Users/bcollins/pyd/library/asyncio-task.html#running-in-threads
'''
def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    with open('/dev/tty2', 'r') as f:
        tty.setraw(f)
        while True:
            print(f.read(1))

def cpu_bound():
    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.
    return sum(i * i for i in range(10 ** 7))

async def main():
    loop = asyncio.get_running_loop()

    ## Options: bc_ seem to each perform well, no clear winner...still a few dropped chars

    # 1. Run in the default loop's executor:
    await loop.run_in_executor( None, blocking_io)
    await loop.run_in_executor( None, blocking_io)
    await loop.run_in_executor( None, blocking_io)
    #print('default thread pool', result)

    # 2. Run in a custom thread pool:
    #with concurrent.futures.ThreadPoolExecutor() as pool:
        #result = await loop.run_in_executor( pool, blocking_io)
    #    print('custom thread pool', result)

    # 3. Run in a custom process pool:
    #with concurrent.futures.ProcessPoolExecutor() as pool:
        #await loop.run_in_executor(pool, blocking_io)
        #await loop.run_in_executor(pool, blocking_io)
    #        # bc_ pool, cpu_bound)
    #    print('custom process pool', result)

asyncio.run(main())
