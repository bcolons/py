from MyP import MyPlinter
class MyStrang(MyPlinter):
    def __init__(self, mys):
        print(f'child has no members prior to super()')
        super().__init__(mys)
        print(f'child has members mys and inp: {self.mys},{self.inp}')
        self.mys=mys
        self.inp=mys
        print(f'child has members mys and inp: {self.mys},{self.inp}')
    def get_mys(self):
        return self.mys
    def sum_dum_fun(self):
        pass
if(__name__=='__main__'):
    m=MyStrang('test..-..test')
    print(f'MyStrang is:{m}\n')

