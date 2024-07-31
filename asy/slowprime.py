import math
class RainTable:
    primes=[] # isPrime bool arr where index represents the actual prime/not prime whole number
    known_pcount=0
    known_npcount=0
    @classmethod
    def testint(self,inp,show_fact=False):
        '''Test for primality via lookup in a rainbow table.
        Add any untested primes encountered.
        Add and then return target primality.
        Do not test any number less than 2. (table is positive primes; divide by zero may be raised)
        show_fact==True will show only the largest factor attempts, inner rainbow table filling is silent.
        '''
        if(RainTable.primes[inp]): # 1. if we tested and stored primality for this inp already, return result
            return RainTable.primes[inp]
        else:
            rootfl=2+math.floor(math.sqrt(inp)) # 2. only need to check 'small' [ <= sqrt(inp)] prime factors, O(root(n)) performance enhancement baby!
            isPrime=True
            for i in range(2,rootfl):
                if(RainTable.primes[i]==None): # 3. number has not yet been prime-tested, test and record it... 
                    RainTable.testint(i,show_fact=False) # only show the latest/farthest-along/biggest factor attempts  
                if(RainTable.primes[i]==True): # 4. if i-th int is not prime, skip it, we will have earlier tried its prime factors...
                    if(show_fact): 
                        print(f'{inp} % {i} == {inp%i}') # logic prints the contgious sequence of non-factor primes up to the final sqrt(inp), nothing more 
                    if(inp % i ==0): # 5. it's a mult of the current prime, we're done for this guy (table may still be missing values...no big deal...)
                        isPrime=False
                        RainTable.primes[inp]=False
                        break
            # we have found a prime in our table which divides inp ('break'); or, we tried everything, loop completes ...inp is actually prime
            # update table, update p and np counts, return primality
            RainTable.primes[inp]=isPrime
            if(isPrime):
                RainTable.known_pcount+=1
            else:
                RainTable.known_npcount+=1
            return isPrime

class PGuess:
    '''Simple impl of an iterator class with one set (Mersenne?) prime guesses.
    Other generator syntax's give __next__ and __iter__ automatically, also dont need class just function (second impl) or gen-expr (third impl).
    '''
    def __init__(self,maxg):
        self.maxg=maxg
        self.current=1
    def __next__(self):
        if(self.current<=self.maxg):
            self.current+=1
            return 1+2**self.current
        else:
            raise StopIteration
    def __iter__(self):
        return self

def pggen(maxg): 
    '''Simple (second) generator impl for PGuess().
    '''
    for i in range(2,maxg):
        yield 1+2**i

for i in range(10**8): # init table
    RainTable.primes.append(None)
RainTable.primes[0]=False
RainTable.primes[1]=False # 1 divides everything... 
RainTable.primes[2]=True
pg = None
maxg=8
#pg=PGuess(maxg) # first impl.
#pg = ( 1+2**i for i in range(2,maxg)) #  Simpler (third) gen-expr impl for class PGuess or func pggen()
#pg = [1+2**i for i in range(2,maxg)] # non-lazy, potentially memory heavy, list comp version
pg=range(2,2**8)

for i in pg: # init first seq of int's...
#for i in pggen(9):
    print(i)
    if(RainTable.testint(i,show_fact=True)):
        print('Prime!')
    else:
        print('...not prime...')
    #if(RainTable.testint(i-2,show_fact=True)):
        #print('Prime!')

print(f'{RainTable.known_pcount} vs {RainTable.known_npcount} ')
