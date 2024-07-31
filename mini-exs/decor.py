class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

@descriptor
class D:
    def __init__(self,num):
        self.num=num
    

class E:
    def __init__(self,num):
        self.num=D(num)
