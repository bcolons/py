class Hashable:
    counter=0
    def __init__(self):
        Hashable.counter+=1
        self.hash=Hashable.counter
    def __hash__(self):
        return self.hash
