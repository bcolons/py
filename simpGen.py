''' Definition: Depending on context 'generator' may mean either: 
        (1) a 'generator function' which returns an instance of an iterator of callables (a 'generator')
        (2) an instance of a generator-iterator, eg. returned from (1); an iterator of callables with arguments (i think...)
        (3) a 'generator object' is the type(..) of object in (2)'''
def print_loop(generator_iterator):
    '''Function that calls-stepwise or iterates over an instance of a generator and prints each result'''
    for val in generator_iterator:
        print(val)

def print_loop_lamda(list_a,lamda_expr):
    '''Function that calls-stepwise or iterates a lambda expression over a list and prints each result'''
    for val in list_a:
        print(lamda_expr(val))
def single_val_generator(list_a):
    """Simplest generator function evah: takes list_a and returns an iterator of square(elem) for each elem"""
    for elem in a:
        yield elem*elem

def two_val_generator(a,b):
    '''Simplest 2 variable generator-iterator, return iterator that call __add__() on stepwise elements of two lists.'''
    for elem in zip(a,b):
        yield elem[0]+elem[1]

a=[1,2,3,4]

print_loop(single_val_generator(a))
print_loop(elem * elem for elem in a) # combining func_args_parens and generator_expression_parens ...very concise!
"""Shorthand for the single_val_generator(): also takes list_a and returns an iterator of square(elem) for each elem """
print_loop(two_val_generator(a,a))
print_loop(elem[0] + elem[1] for elem in zip(a,a)) # combining func_args_parens and generator_expression_parens ...very concise!
"""Shorthand for the two_val_generator(): also takes list_a and returns an iterator of square(elem) for each elem """
print_loop_lamda(a,(lambda x:  x+x))
print( [(lambda x : (yield x +3))(y) for y in range(2) ]) # list comp with lambda creating generator-iterator instance
'''Lamda shorthand for the two_val_generator() and generator function shorthand'''
print((lambda x: x+x)(99))
print(two_val_generator(2,3))
asdf=two_val_generator(a,a)
print(next(asdf))
print(asdf)
# (elem * elem for elem in a) 

