import json
import inspect
class Obj():
    def __init__(self):
        self.summem="asdfa"
    def sumfun(self):
        pass
    def dumpstate(self,d):
        captured=False
        print(f"to begin with d is: {str(type(d))}")
"""
        if(str(type(d)) == "<class 'dict'>"):
            captured=True
            print(f"dict-black, captured is {captured}")
            k = d.keys()
            for i in k:
                print(f"{str(i)}:{str(d[i])}")
                print(f"{str(type(i))}:{str(type(d[i]))}")
        elif(not captured):
            try:
                b=["<class 'str'>" , "<class 'list'>"].index(str(type(d)))
                captured=True
                for i in range(len(d)):
                    print(f"str/list block, captured is {captured},{d[i]}")
            except ValueError:
                print("not str or list")
                print(f"str/list except , captured is {captured}")
            try:
                b=[ "<class 'tuple'>", "<class 'set'>"].index(str(type(d)))
                captured=True
                for i in iter(d):
                    print(f"tup/set block , captured is {captured}, {i}")
            except ValueError:
                print("not tuple or set")
                print(f"tup/set except , captured is {captured}")
        if(not captured):
            captured=True
            print(f"finally prim/Obj block , captured is {captured}")
            print("object:"+str(d))
            meths=inspect.getmembers(d)
            print("meths:" +str(meths))


if(__name__=='__main__'):
    d = {"hey":"you","one":1, "z":{"e":"e","b":"b","r":"a"}}
    d = "a","sdfafd"
    d = ["a","sdfafd"]
    d = {"a","sdfafd"}
    d ="str primitve"
    d = 987
    d = Obj()

    o=Obj()
    o.dumpstate(d)
"""
