import collections.abc as abc
import random as r
class Randomizer(abc.Callable):
    def __init__(self):
        self.string=str(r.random())
    def __call__(self):
        self.string=str(r.random())
myr=Randomizer()
print(myr.string)
myr()
print(myr.string)
