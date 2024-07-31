class myc:
    def __init__(self,data):
        self.data=data
        if not self.count: 
            self.count=0
        self.count+=1
    def __copy__(self):
        return self.data, self.count
if(__name__=='__main__'):
    a=myc('hey')
