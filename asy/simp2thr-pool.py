from multiprocessing import Pool, TimeoutError
import time
import os
''' from:
    file:///C:/Users/bcollins/pyd/library/multiprocessing.html#using-a-pool-of-workers
'''
def f(x):
    time.sleep(1)
    print(time.time())
    return x*x

if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        print('15: '+str(pool.map(f, range(10))))

        # print same numbers in arbitrary order
        for i in pool.imap_unordered(f, range(10)):
            print('19: '+str(i))

        # evaluate "f(20)" asynchronously
        res = pool.apply_async(f, (20,))      # runs in *only* one process
        print('23: '+str(res.get(timeout=1)))             # prints "400")

        # evaluate "os.getpid()" asynchronously
        res = pool.apply_async(os.getpid, ()) # runs in *only* one process
        print('27: '+str(res.get(timeout=1)))             # prints the PID of that process

        # launching multiple evaluations asynchronously *may* use more processes
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print(['31: '+str(res.get(timeout=1)) for res in multiple_results])

        # make a single worker sleep for 10 secs
        res = pool.apply_async(time.sleep, (10,))
        try:
            print('36: '+str(res.get(timeout=1)))
        except TimeoutError:
            print("38: We lacked patience and got a multiprocessing.TimeoutError")

        print("40: For the moment, the pool remains available for more work")

    # exiting the 'with'-block has stopped the pool
    print("43: Now the pool is closed and no longer available")
''' output:
15: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
19: 0
19: 1
19: 4
19: 16
19: 25
19: 36
19: 49
19: 64
19: 81
19: 9
23: 400
27: 273
['31: 272', '31: 275', '31: 274', '31: 273']
38: We lacked patience and got a multiprocessing.TimeoutError
40: For the moment, the pool remains available for more work
43: Now the pool is closed and no longer available
'''
