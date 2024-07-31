class TrNod:
    cache=[] # in order sequence of TrNod's with the prior searched string's matching prefix nodes 
    # search_memo()-cache_suff() not threadsafe, 
    # must lock incoherent cache between search_memo()-truncate and return of cach_suff() after completed update
    def __init__(s,ch=''):
        s.ch=ch
        s.arr=[]
        s.funcarr = [s.search,  s.search_memo, s.search_memopy]
    def __lt__(s,t):
        """Each TrNod list is kept in alphabetical order for a (not_implemented) mergesort-style logN-time search """
        return s.ch < t.ch
    def init_cache(root_node):
        """Initialize search_memo()'s prior TrNod list (the 'cache tree' ) as TrNod.cache=[root_node]"""
        TrNod.cache.append(root_node)
    def chsearch(self,inp):
        """Check the first char of inp for a match in a single ('child node') TrNod.arr
        Returns first matched child TrNod ref or else False
        To get a matching child TrNod (or False) for inp[0] call as:
            childTN = node.chsearch(inp) """
        for child in iter(self.arr):
            if child.ch==inp[0]:
                return child # first char matched this child TrNod
        return False
        
    def search_memopy(self,suff): # more pythonic search_memo()
        elem=TrNod.cache[0]
        print('suff len '+str(len(suff))+ ' , ' + str(len(TrNod.cache)))
        for ix in range(len(TrNod.cache[1:])):
            print('ix: '+str(ix))#+' , suff[ix]: '(suff[ix]))
            if(suff[ix]!=TrNod.cache[ix+1]): # TrNod.cache has initial '' unlike any intial suff char
                TrNod.cache=TrNod.cache[:ix+1] # truncate any following (ie non-matching) TrNod's from cache list
                return TrNod.cache[ix+1].cache_suff(suff[ix]) # delegate a recursive main tree search, caching each matching char along the way
                break # not necessary ?
    def search_memo(self,suff): # try for a closer to linear search for spatial/temporal -ly local (a-z sorted) inputs
        """Cache-optimized alternate to search() for a-z pre-sorted sequences of strings
        Each char from the prior search_memo() is in the 'cached tree' (merely a prefix char list), each match avoids a 26-way main tree search.
        Usage identical to search() and requires terminal '$' on input.
        search_memo():
            loops over TrNod.cache for the last matching prefix char's TrNod, 
            once found, truncates TrNod.cache's remaining non-matching TrNod's
            calls recursive:
                node,suff = last_matched_node.cache_suff(suff) which: 
                    updates TrNod.cache with each matching suffix char from the main tree TrNod, 
                    returns node,suff of last main tree match same as search() and search_memo() """
        ix=0 # == TrNod.cache.index(TrNod('')) ie the root node, this index will trim cache after the last hit
        elem=TrNod.cache[0] # cache tree root node ''
        for elem in iter(TrNod.cache[1:]): # '' is initial / root char in cache, input string never has this. Also indexes are aligned btwn suff and TrNod.cache[1:]
            if(suff[ix]==elem.ch): # if( first node in cache == first char in string ) -> cache hit
                ix+=1 # if we trim now slice is TrNod.cache[:ix]
                print('cache hit! at  elem.ch: '+elem.ch+', '+ 'suff['+str(ix)+']: '+elem.ch)
                continue # only start into main_tree.search() once we have the last cached matching TrNod
            else: # remaining novel suffix is delegated to recursive cache_suff 
                break
        TrNod.cache=TrNod.cache[:ix+1] # truncate the cache to the matching prefix just before miss, TrNod.cache index is one higher than suff[ix]
        return elem.cache_suff(suff[ix:]) # jump across to characterwise main_tree.search(), to facilitate charwise caching; returns final return of search()
    def cache_suff(self,suff):
        """
        Updates the suffix of TrNod.cache with remaining TrNod refs in a loop via:
            Characterwise search() in tree, TrNod.cache.append( each matched TrNod )
            Returns last matching (node,suff) ie. same return case/vals as search() and search_memo()"""
        if(not suff):
            return (self,suff)
        node,suff_None=self.search(suff[0]) # suff_None is always None because suff[0] is a single elem
        if(node.ch==suff[0]):
            TrNod.cache.append(node) # add matching child TrNod to cache
            return node.cache_suff(suff[1:])
        else:   
            return (self,suff)
            
    def search(self,suff): 
        """ Searches recursively for a string/prefix match and returns (novel suffix , last matching prefix character node )
        Returns: ( node,    # TrNod ref for last of successively matched prefix chars
                   suff  )  # novel suffix past last matching char
        Recurses via: node.search(suff)
        Call with $ input string terminator (" inp$ ") except to delete() a terminating $ node  use " inp_no$ " instead
        To spellcheck a string, call as root_node.search( inp$ ) 
        A full match will return 
            (  a TrNod_ref with self.ch=='$', '' ) 
        An input which fully matches a tree prefix will return 
            (  a TrNod_ref with self.ch=='last_matching_prefix_char', '' ) 
        An input which has a matching prefix and a novel suffix will return 
            ( a TrNod_ref with self.ch=='last_matching_prefix_char', novel_suff ) 
        Use return tuple to add() and delete() words from tree."""
        if(not suff): # must have matched all the way to end of input
            # if terminal $ was stripped, caller may now self.delete() which calls self.arr.remove(TrNod('$'))
            return (self,suff) #suff is False here, out of novel suffix characters
        child=self.chsearch(suff) # try find a match child node for initial remaining char at this level
        if(not child): # False means no matching chars at this level, 
            #caller may now self.add(suff) to go under self.arr
            return (self,suff)
        else: 
            return child.search(suff[1:]) # recurse w rest of novel suffix and child TrNod

    def delete(self): 
        """Demote a string from valid to invalid by deleting terminal $ node from tree
        Caller must strip terminal $ to find parent of terminal $ 
        Call as:
            (1) node,suff = root_node.search( inp_no$ ) # to get parentnode.arr (ignore suff)
            (2) node.delete() # will delete terminal TrNod('$') leaving a potentially valid (or not) 
                prefix to other (or no) existing $ terminated words---valid words always have final $, 
                though the tree is not required to have $-leaves/terminals (tree may have orphan prefixes) """
        term_dollar_node=self.chsearch('$')
        try:
            self.arr.remove(term_dollar_node) #gc does the rest
        except ValueError:
            pass #remove() tried to delete something which doesnt exist

    def add(self, suff): 
        """ Recursive/telescoping single-initial-char insert method
        Call as:
            (1) node,suff = search( inp$ ) # returns node with matching prefix
            (2) node.add( suff ) # adds telescoping branch under node.arr """
        try: #empty suff raises IxErr which happens for search(duplicate_string)
            newnode=TrNod(suff[0]) #empty str raises IxErr
            self.arr.append(newnode)
            self.arr.sort()
            if(suff[1:]):
                newnode.add(suff[1:]) #else we've added chars all the way to final $
        except IndexError:
            pass
    def tos(s,string_buffer,indent=-1):
        """Recursively to-string the entire TrNod tree characters with dot-indent to show depth level.
        Called from self.dump() as self.tos(string_buffer=['\\n']) """
        string_buffer+=s.ch
        if(s.arr):
            indent+=1
            string_buffer+="<"+'.'*indent
            for child in iter(s.arr):
                child.tos(string_buffer,indent)
            string_buffer+="."*indent+">"
        return str(string_buffer)
    def dump(self,string_buffer=None):
        """Print entire tree under a node without commas, quotes or newlines. 
        Calls self.tos() to format with angle brackets and dot-indenting to show depth level.
        For entire tree call as: root_node.dump() """
        if(string_buffer==None):
            string_buffer=["\n"]
        self.tos(string_buffer)
        for elem in string_buffer:
            print(elem,end='')
    def insert(s,inp=[]):
        """User-friendly bulk wrapper for search() and add().
        Duplicate strings are silently ignored.
        Terminal '$' on inputs will be added.
        Call as: root_node.insert(['mystring','someother'])  """
        for elem in inp:
            node,suff=s.search(elem+'$')
            node.add(suff)
    def delstr(s,inp=[]):
        """User-friendly wrapper for bulk search() and delete() 
        No terminal '$' on input.
        Missing strings are silently ignored.
        Call as: root_node.delstr(['mystring','someother'])"""
        for elem in inp:
            node,suff=s.search(elem[:-1])
            node.delete()

    def test(self):
        a=TrNod('')
        b=TrNod('')
        c=TrNod('')
        a.init_cache()
        b.init_cache()
        c.init_cache()
        inp = ['a$','ab$', 'abc$', 'az$']
        rootarr = [a, b,c]
        for i in range(len(rootarr)-1):
            for elem in inp:
                node,suff=rootarr[i].funcarr[i](elem)
                print(str(i)+'('+elem+') returns --> node,suff '+str(node.ch)+','+str(suff))
                node.add(suff)
                rootarr[i].dump()
                print('cache: ',end='')
                for each in rootarr[i].cache:
                    print(each.ch,end=' ' )
                print()
z=TrNod('z')
z.test()
print()
