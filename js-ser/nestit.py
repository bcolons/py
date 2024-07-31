def mainfun( curit, parit):    
    n=None
    try:
        n=next(curit) #raises StopIteration if not another elem or iterable
        print("n is: "+n)
        mainfun(curit)
        return
    except TypeError as te: # must be something to cast as iterable
        print('typeerr: current n is: '+str(n))
        mainfun(iter(n)) # descend into to inner iterable
        return
    except StopIteration as si: # next() raises no more elems
        print('StopIter: current n is: '+str(n))
        return #off the end of some inner or outermost iterable
if(__name__=='__main__'):
    print("yeah...")
    a ="a","b","c"
    d = a,"e","f",a # (a,b,c),e,f,(a,b,c)
    g = d,a,(d,a),d
    z = ((('a','b'),'c',(('d','e'),'f'),'g'),('h',('i','j'),'k'),'l')
# m(z)
# m(a-g)
# m(a-f)
# m(a-e)
# m(a-b)
# m(a) -> a
# m(b) -> b
# m(b++) -> return
# m(c) -> c
# m(c++) -> retirn
# m(d-e)
# m(d) -> d
# m(e) -> e
# m(e++) -> return
# m(f) -> f
# m(f++) -> return
# m(g) -> g
# m(g++) -> return
# m(h-k) 
# m(h) -> h
# m(i-j) 
# m(i) -> i
# m(j) ->j
# m(j++) -> return
# m(k) -> k
# m(k++) -> return
# m(l) -> l
# m(l++) -> return
    print("fulltree is: "+str(z)+"\n\n")
    """
    for zz in iter(z):
        try:
            print("zz: "+ zz)
        except TypeError:
            for yy in iter(zz):
                try:
                    print("yy: "+yy)
                except TypeError:
                    for xx in iter(yy):
                        try:
                            print("yy: "+yy)
                        except TypeError:
                            print('tired of this manual shit...')
    print("...off the end")
    """
    mainfun(iter(z))


    n='n not set'
    p='p not set'
# cast toplevel to iter
# next(tl) will give:
# 1. primitive 
# or
# 2. something which can be cast as iter (case it out or except raised TypeError)
# or
# 3. raise StopIteration on any final elem
#if:
#1. print it, try next(..) (ie. reurse(curit)
#2.dont print anything, cast elem as iter, try next(iter(elem)) (ie. recurse)
#3. except StopIteration then return

