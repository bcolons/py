class MyPlinter():
    def __init__(self,i):
        self.inp='my '+i+' Printed'
        print(f'in is {self.inp}\n')
        self.mys=None

if(__name__ == '__main__'):
    m=MyPlinter('hiya')
    print (f'hey i"m {m.inp}\n')
    print(f'MyPrinter is:{m.mys}\n')

