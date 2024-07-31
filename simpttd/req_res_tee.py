import sys
import bc_req_res
class TWr:
    def __init__(self):
        self.arch=bc_req_res.ReqResArch()
    def arch_req_res(self, rawreqline,res='most_recent'):
        '''Copy request lines to persistent archive streams (sto,sto2) from one reader stream, stin.
        Calls stin.read() and sto*.write() so must exist'''
        self.arch.data[str(rawreqline)]=res

if( __name__=='__main__'):
    with open(sys.argv[1], 'r') as r:
        with open(sys.argv[2], 'w') as w1:
            with open(sys.argv[3], 'w') as w2:
                teewrite(r,w1,w2)
