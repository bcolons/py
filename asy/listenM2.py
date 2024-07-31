import time as t
import multiprocessing
'''Simple way to run a system in another process and then enter a char-interactive listener method to examine members and call methods in realtime. bc_ doesnt have shared mem...
'''
class ListeninMixin:
    '''Class which supplies: 
        1. a template, listen(), to capture user keystrokes and return a main class data member or call method in real time.
        2. a target, start_threads(), to start main and listener via: asyncio.run(..)
    '''
    def listen(self):
        '''Representative notional template method which is called to start the listener thread.
        Register single character inputs and configure sbsq listening behaviour: print member data or call a method.
        '''
        while True: # thread raises IndexError if naked newline entered
            inp=input()
            if inp[0] == 'r':
                print('runsum: '+str(self.runsum))
            elif inp[0] == 'p':
                print(f'__{self.i}__ i heard it through the grapevine: '+inp)
            elif inp[0] == 'q': #quit
                break #raise KeyboardInterrupt
            elif inp[0] == 'a': #active count
                print(f'active_count(): {threading.active_count()}')
            #elif inp[0]=='k': # kill all
            #    for each in threading.enumerate():
            #        each.join(timeout=1)


# BEGIN ---- the main system ----
class Obj(ListeninMixin):
    '''Representative notional template class.
    Members and methods are available to listener thread.
    '''
    def __init__(self):
        '''Constructor defines main members and any listener-helper members. 
        '''
        self.i=None
        self.runsum=0
    def main(self):
        '''Representative notional template method which is called to start the main thread.
        '''
        for self.i in range(3):
            print(f'{self.i} ninths the way there!')
            self.updatesum(self.i)
            t.sleep(1)    # placeholder for any slow computation we might want to check in on without disruption (readonly! as not thsafe)
    def updatesum(self,i):
       '''Shows listener can call methods and corrupt data without any obvious safety mechanism (in Python).
       '''
       self.runsum+=i 
# END ---- the main system ----

obj=Obj()
multiprocessing.Process(target=obj.main).start()
obj.listen()
