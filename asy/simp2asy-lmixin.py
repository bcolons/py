import asyncio
import time as t
'''Simple way to run a system in a thread and run a char-interactive listener thread to examine members and call methods in realtime.
'''
class ListeninMixin:
    '''Class which supplies: 
        1. a template method, listen(), to capture user keystrokes and return a main class data member or call method in real time.
        2. a target method start_threads to start main and listener via last line: asyncio.run(..)
    '''
    def listen(self):
        while True:
            inp=input()
            if inp[0] == 'r':
                print('runsum: '+str(self.runsum))
            elif inp[0] == 'p':
                print(f'__{self.i}__ i heard it through the grapevine: '+inp)
            else:
                pass

    async def start_threads(self):
        await asyncio.gather(
            asyncio.to_thread(self.crunch),
            asyncio.to_thread(self.listen),)


# BEGIN ---- the main system ----
class Obj(ListeninMixin):
    def __init__(self):
        self.i=None
        self.runsum=0
    def crunch(self):
        for self.i in range(9):
            print(f'{self.i} ninths the way there!')
            self.updatesum(self.i)
            t.sleep(1)    # placeholder for any slow computation we might want to check in on without disruption (readonly! as not thsafe)
    def updatesum(self,i):
       self.runsum+=i 
# END ---- the main system ----

asyncio.run(Obj().start_threads())
