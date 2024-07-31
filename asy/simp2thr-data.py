import threading
import time as t
'''Simplest way to run one method alongside a listening method with a common non-primitive data struct shared and thr4 listenable.
'''
def listen(d):
    while True:
        inp=input()
        print(f'__{d[0]}__ i heard it through the grapevine: '+inp)
def crunch(d):
    for i in range(9):
        d[0]=i
        print(f'{i} ninths the way there!')
        t.sleep(1)    # placeholder for any slow computation we might want to check in on without disturbing (not thsafe)
d=[0]
listener=threading.Thread(target=listen,args=(d,))
cruncher=threading.Thread(target=crunch,args=(d,))
cruncher.start()
listener.start()
