import time
import threading
import inspect
import bc

class Mythr():
    threadarr=[]
    def __init__(self,period):
        Mythr.threadarr.append(self)
        self.period=period
    def startup(self):
        print(bc.ppp_s(inspect.currentframe()))
        print(inspect.stack())
        print(inspect.trace())
        while True:
            time.sleep(self.period)
myt=Mythr(1)
t1=threading.Thread(target=myt.startup)
t1.start()
        
    
