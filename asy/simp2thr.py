import threading
import time as t
def listen():
    while True:
        inp=input()
        print('i heard it through the grapevine: '+inp)
def crunch():
    for i in range(9):
        print(f'{i} ninths the way there!')
        t.sleep(1)    
listener=threading.Thread(target=listen)
cruncher=threading.Thread(target=crunch)
cruncher.start()
listener.start()
