class DoubD:
    '''Dictionary which allows random access of keys and values (both must be hashable and neither mutated; Fixme: allow mutations, detect them and rebuild appropriate index)
    Use case: want to be able to search on keys as normal as well as find a unique value token for an incomplete pair: key/'dummy' for completion. 
    This class was designed to cache a request and then a later subsequent response from an existing and mostly unmodified http.server instance.
    This class effectively changes builtin dict.update(..) to a private method which allows committing a request with a response placeholder prior to response string completion'''
    def __init__(self):
        self.dd={}
        self.dd_inv={} # this guy uses values() to index keys()
    def ins_k_v(self, key, val='dummy'):
        '''Main way to index response strings by their request keys (for example)'''
        self.dd.update([(key, val)])
        self.dd_inv.update([( val, key)]) # raises error if more than one 'dummy' val, dup keys overwrite
    def ins_v_k(self, val, key='dummy'):
        '''Need this to complete the pair using 'dummy' as the key. '''
        self.dd.update([(key, val)])
        self.dd_inv.update( [(val, key)] ) # raises error if more than one 'dummy' key, dup vals overwrite
    def sel_k(self, key):
        '''Returns a response string selected by request (for example)'''
        return self.dd[key]
    def __str__(self):
        '''Dump both underlying dict's for qa purposes.'''
        sbuf=''
        for each in self.dd:
            sbuf+=each+':'+self.dd[each] + ', '
        for each in self.dd_inv:
            sbuf+=each+':'+self.dd_inv[each] + ', '
        return sbuf

if(__name__=='__main__'):
    a=DoubD()
    a.ins_k_v('key1','val1')
    a.ins_k_v('key2','val2')
    a.ins_v_k('val3')
    print(a)
