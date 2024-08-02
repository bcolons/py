import sys

doubled={'c':{'a':'aa','b':'bb'},'d':{'a':'aaa','b':'bbb'}} #test dicts

def invd(d):
    dout=dict()
    for each in d.keys():
        dout.add((d[each],each))
    return dout

def byte_it():
    inp=True
    while inp:
        inp=sys.stdin.read(1) #False when EOF read
        if not inp:
            raise StopIteration
        else:
            yield inp

def trans(keyd,char):
    invdict=invd(keyd)
    try:    
        outchar=keyd[char]
        sys.stdout.write(outchar)
        try:    
            sys.stdout.write(invdict[outchar])
        except KeyError:
            sys.stdout.write('invfail ')
    except KeyError:
        sys.stdout.write(inp)
    sys.stdout.flush()
for each in byte_it():
       trans(doubled['d'],each)
