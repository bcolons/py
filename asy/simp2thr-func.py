import threading
import time as t
'''Simplest way to run one method alongside a listening method with a common non-primitive data struct shared and thr4 listenable.
bc_ doesnt work concurrently...t1 and then t2 or v/v
'''
class ListeninMixin:
    def listen(self):
        while True:
            inp=input()
            print(f'__{self.i}__ i heard it through the grapevine: '+inp)
            if inp == 'q': 
                break

class Obj(ListeninMixin):
    def __init__(self):
        self.i=None
    def crunch(self):
        for self.i in range(9):
            print(f'{self.i} ninths the way there!')
            t.sleep(1)    # placeholder for any slow computation we might want to check in on without disturbing (not thsafe)

obj=Obj()
t2=threading.Thread(target=obj.listen()) # gives us a self ref and we can see all Obj members
t1=threading.Thread(target=obj.crunch())
t2.start()
t1.start()
