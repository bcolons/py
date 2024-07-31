import sys
def teewrite(stin,sto,sto2):
    '''Write to two identical writer streams (sto,sto2) from one reader stream, stin.
    Calls stin.read() and sto*.write() so must exist'''
    temp=stin.read()
    sto.write(temp)
    sto2.write(temp)

if( __name__=='__main__'):
    with open(sys.argv[1], 'r') as r:
        with open(sys.argv[2], 'w') as w1:
            with open(sys.argv[3], 'w') as w2:
                teewrite(r,w1,w2)
