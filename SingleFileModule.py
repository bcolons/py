'Module stuff here... top level __doc__ string (must be first statement in file)'

#mod_name = __package__ is the toplevel ref, runpy.run_module(mod_name) loads and runs mod at r/t plus other shit
# noargs dir() returns a module's attrs, ow applies to an obj
# noargs __doc__ , obj.__doc__ return docstring for class/type

class MyPar:
    'Doc strang! (not inher d)'
    def __init__(self):
        self.i=3
        self.b=True
        self.s='par string'

class MyChi(MyPar):

    def __init__(self):
        super.__init__(super)
        self.k='ijk'

def maine():
    print('hey')
