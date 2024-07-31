import json
import doctest
import partd
class ReqResArch(partd.PartD): #ins_k_v(..), ins_v_k(..), sel_k(..)
    '''Class file-persists a contained PartD or 'req/res dict which supports partial pair of just req' for use to cache I/O for a blocking/singlethreaded http.server.
    All record specific methods belong to sub class PartD.'''
    def __init__(self):
        '''Open and load file archive.'''
        with open('bc_req_res.json','r')  as fdr:
            #whole_arch='{"a":"apple"}'
            whole_arch=fdr.read()
            self.dd=json.JSONDecoder().decode(whole_arch)
        for each in self.dd:
            self.dd_inv=self.dd[each]=each

    def sync(self):
        '''Open and write file archive'''
        with open('bc_req_res.json','w') as fdw:
            fdw.write(json.JSONEncoder().encode(super.dd))
    def dump(self):
        '''Display archive for sanity checking.'''
        rqrsa=ReqResArch()
        rqrsa.sync()
        for k in rqrsa.dd:
            print('k: '+k+' v: '+rqrsa.dd[k])

if(__name__=='__main__'):
    d=PartD()
    d.dd={'d':'dog','e':'egg'}
    d.sync()
    print('rqrsa.dd is: ')
    for k in d.dd:
        print('k: '+k+' v: '+d.dd[k])

    
