import shutil
import sys

class cp:
    #@staticmethod
    def __init__(self): #py -i
        shutil.copyfileobj(sys.stdin,sys.stdout)
