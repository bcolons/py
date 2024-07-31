import subprocess as sub 
import sys 
import os

class star:
    """
    Execute a shell command iterating over input filenames (skipping argv[0] the python exectuable).
    """
    def funwun(s,t):
        return s+t
print(sys.argv[1:])
for filename in sys.argv[1:]:
    if(filename):
        try:
            #sub.call(['links','-dump',filename, f'>{filename}.py'])
            #   ...is too smart...complains about shell operators like | and > 
            print('about toe run: '+ str('links'+' -dump '+filename+'>'+filename+'.py'))
            os.system(str('links'+' -dump '+filename+'>'+filename+'.py'))
        except IsADirectoryError:
            print('directory! err: '+filename) 
        except UnicodeDecodeError:
            print('unicode dec err: '+filename) 
        except PermissionError:
            print('permish err: '+filename)
