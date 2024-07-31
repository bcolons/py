'''Docnot'''
import inspect
# mod_name = __package__ is the toplevel ref, runpy.run_module(mod_name) loads and runs mod at r/t plus other shit
# importlib.reload(mod_name) to inval cache and get a fresh mod ver
# sys.builtin_module_names is first stop for 'import' then sys.path: cur dir plus env py path dirs and site-packages
# noargs dir() returns a cur defined attrs minus builtins; ow applies to an obj or module
# noargs __doc__ , obj.__doc__ return docstring for class/type
# package.submodule (dir.file req __init__.py; 'import submod1'  or  define __all__ = ['modulenam1','modname2'] for from blah import * )
# 
class MyPar:
    '''Doc strang!'''
    def __init__(self):
        self.i=3
        self.b=True
        self.s='par string'

class MyChi(MyPar):

    def __init__(self):
        self.k='ijk'
        super().__init__()

def main():
    print('hey')
