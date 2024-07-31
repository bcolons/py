import multiprocessing
import time
def lp(arg):
    while True:
        print(str(arg))
        time.sleep(arg)
multiprocessing.Process(target=lp,args=(1,)).start()
multiprocessing.Process(target=lp,args=(2,)).start()
multiprocessing.Process(target=lp,args=(3,)).start()
