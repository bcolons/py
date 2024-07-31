import sys
class WithEx:
    def __init__(s):
        pass

#if(__name__=='__main__'):
try:
    with open(sys.argv[1],'r') as file:
        print(file.read())
except FileNotFoundError:
    pass
