class Int:
    def __init__(self,i):
        self.i=i
    def __eq__(self,obj):
        return self.i == obj.i
    def __hash__(self):
        return hash(self.i)
