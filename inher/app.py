import .bcdeep.Barf
class Par:
    def __init__(self):
        self.data='pardata' #overwritten by subclass cons if collision or else not
        self.pd={'pa':'papple','pb':'pbear'}
    def sumfun(self):
        return 'par\n'
    def sumParOnlyMeth(self):
        pass

class Chi(Par):
    def __init__(self):
        self.data='chidata'
        self.cd={'ca':'capple','cb':'cbear'}
        super()
    def sumfun(self):
        return super().sumfun() #'child\n'
if(__name__=='__main__'):
    c=Chi()
    print(c.data)
    print(c.sumfun())
