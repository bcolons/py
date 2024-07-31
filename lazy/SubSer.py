import json
class SubSer(json.JSONEncoder):
    def default(self, o):
       try:
           iterable = iter(o)
       except TypeError:
           pass
       else:
            return list(iterable)
            #return json.JSONEncoder.default(self, iterable)
       # Let the base class default method raise the TypeError
       try:
            return json.JSONEncoder.default(self, o.__str__())
       except BaseException:
            print('errstr')
       return json.JSONEncoder.default(self, o)

class Nodes():
    class Node(str):
        def __init__(self,string):
            self.data=string
        def __str__(self):
            return self.data
    def __init__(self):
        self.nodes=[]
    def add(self,string):
        self.nodes.append(self.Node(string))
        return self
    def __iter__(self): # must return iter of primitives
        it=[]
        for each in self.nodes:
            it.append(each.__str__())
        return iter(it)
        

ns=Nodes()
ns.add('i').add('am')
print(SubSer().encode(ns))

