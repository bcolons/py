# type annotations in use!
from dataclasses import dataclass
@dataclass
class SomeData:
    ct: int # automatically creates __init__(self,ct,price) : ...
    price: float
    def tot(self):
        return self.ct*self.price
# example shows inheritance and position/vs kw only annotations and behavior
@dataclass
class Base:
    x: Any = 15.0
    _: KW_ONLY # just like '*' in an explicit constructor
    y: int = 0
    w: int = 1

@dataclass
class D(Base):
    z: int = 10
    t: int = field(kw_only=True, default=0)
# generated D constructor is:
# def __init__(self, x: Any = 15.0, z: int = 10, *, y: int = 0, w: int = 1, t: int = 0):

