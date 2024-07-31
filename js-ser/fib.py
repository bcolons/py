def fib_rec(num):
    if(num!=0 and num !=-1):
        new=fib_rec(num-1) +fib_rec(num-2)
        print(new)
        return new 
    else:
        return 1

if(__name__=='__main__'):
    print(fib_rec(9))

# 1,1,2,3,5,8,13

#fib(1)==1
#fib(2)==1+1
#fib(1)==1
#fib(1)==1
#fib(1)==1
#fib(1)==1
#fib(1)==1

