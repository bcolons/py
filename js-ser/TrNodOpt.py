class TrNod:
    """Optimized TrNod class which uses a cache TrNod tree to maintain a tiny lookaside buffer with nodes for last search_memo()"""
    cache=None # TrNod 'tree' with the prior searched string's matching prefix nodes ie its a linked list
    """ search_memo()-cache_suff() not threadsafe, 
    # must lock incoherent cache between search_memo()-truncate and return of cach_suff() after completed update"""
    def __init__(s,ch=''):
        s.ch=ch
        s.arr=[]
    def __lt__(s,t):
        """Each TrNod list is kept in alphabetical order for a (not_implemented) mergesort-style logN-time search """
        return s.ch < t.ch
    @staticmethod
    def init_cache(): 
        """Initialize search_memo()'s 'prior TrNod cache tree' root node."""
        TrNod.cache = TrNod('')
    def chsearch(self,inp):
        """Check the first char of inp for a match in a single ('child node') TrNod.arr
        Returns first matched child TrNod ref or else False
        To get a matching child TrNod (or False) for inp[0] call as:
            childTN = node.chsearch(inp) """
        for child in iter(self.arr):
            if child.ch==inp[0]: # first char matched this child TrNod
                return child 
        return False
        
    def clonechild(self,char):
        """Returns a new TrNod with self.arr."""
        pass
    def search_memo(self,full_suff): # try for a closer to linear search for spatial/temporal -ly local (a-z sorted) inputs
        """Cache-optimized alternate to search() for a-z pre-sorted sequences of strings
        Each char from the prior search_memo() has a TrNod in the 'cached tree'  each match avoids a 26-way main tree search.
        Usage identical to search() and requires terminal '$' on input.
        search_memo(): #non-mutating except to clear last matching TrNod's .arr FIXME 
            traverses TrNod.cache for the last matching prefix char's TrNod.ch, 
            once found, traverses main tree from ref in matchingTrNod.arr
            calls recursive:
                suff,node = last_matched_node.cache_suff(suff) which is mutating and ....:  
                    adds new nodes to TrNod.cache with each matching suffix char from the main tree TrNod, 
                    returns suff,node of last main tree match same as search() and search_memo() """
        cache_novel_suff,last_cache_hit_node = TrNod.cache.search(full_suff)  # traverse and match the linked list of copies of TrNod's, one for each char in last search_memo()
        last_cache_hit_node.arr=[] # free non-matching suffix child array FIXME
        return  last_cache_hit_node.cache_suff(cache_novel_suff) # node is a copy with a copy of links to main tree, return val is:  (main_novel_suff,last_matched_main_node )
    def cache_suff(self,suff): # initial called with suff as cache_miss_suff
        """
        Updates TrNod.cache tree with copies of any remaining matching char's TrNod refs in a loop via:
            Characterwise search() in tree, TrNod.cache.add( copy of each matched TrNod )
            Returns last matching (suff,node) ie. same return case/vals as search() and search_memo()"""
        suff_None,node=self.search(suff[0]) #suff_None is always None because suff[0] is a single elem
        if(node.ch==suff[0]):
            newCacheTN=TrNod(node.ch) #copy key char
            newCacheTN.arr=node.arr.copy() # clone child array
            self.addTrNod(newCacheTN) # add copy of matching child TrNod to cache tree
            return node.cache_suff(suff[1:]) # Recurse along main tree
        else:  # Recursion returns, main tree doesn't match this suffix any further, caller may self.add(suff) to main tree (though add() does not memo-ize new TrNod's 
            return (suff,self)
            
    def search(self,suff): 
        """ Searches recursively for a string/prefix match and returns (novel suffix , last matching prefix character node )
        Returns: ( suff,   # novel suffix past last matching char
                   node  ) # TrNod ref for last of successively matched prefix chars
        Recurses via: node.search(suff)
        Call with $ input string terminator (" inp$ ") except to delete() a terminating $ node  use " inp_no$ " instead
        To spellcheck a string, call as root_node.search( inp$ ) 
        A full match will return 
            ( '' , a TrNod_ref with self.ch=='$' ) 
        An input which fully matches a tree prefix will return 
            ( '' , a TrNod_ref with self.ch=='last_matching_prefix_char' ) 
        An input which has a matching prefix and a novel suffix will return 
            ( 'novel_suff' , a TrNod_ref with self.ch=='last_matching_prefix_char' ) 
        Use return tuple to add() and delete() words from tree."""
        if(not suff): # must have matched all the way to end of input
            # if terminal $ was stripped, caller may now self.delete() which calls self.arr.remove(TrNod('$'))
            return (suff,self) #suff is False here, out of novel suffix characters
        child=self.chsearch(suff) # try find a match child node for initial remaining char at this level
        if(not child): # Recursion returns. False means no matching chars at this level, caller may now self.add(suff) to go under self.arr
            return (suff,self)
        else: 
            return child.search(suff[1:]) # Recurse w rest of novel suffix and child TrNod

    def delete(self,terminal_char='$'): 
        """Demote a string from valid to invalid by deleting terminal $ node from tree
        Caller must strip terminal $ to find parent of terminal $ 
        Call as:
            (1) suff,node = root_node.search( inp_no$ ) # to get parentnode.arr (ignore suff)
            (2) node.delete() # will delete terminal TrNod('$') leaving a potentially valid (or not) 
                prefix to other (or no) existing $ terminated words---valid words always have final $, 
                though the tree is not required to have $-leaves/terminals (tree may have orphan prefixes)
        Alternately call TrNod.cache.index(one_beyond_last_match_node).delete() to trim TrNod.cache branch past last matching node"""
        term_node=self.chsearch(terminal_char)
        try:
            self.arr.remove(term_node) #gc does the rest
        except ValueError:
            pass #remove() tried to delete something which doesnt exist

    def addTrNod(self,child):
        """Append a child to a self/parent's TrNod arr."""
        self.arr.append(child)
    def add(self, suff): 
        """ Recursive/telescoping single-initial-char insert method
        Call as:
            (1) suff,node = search( inp$ ) # returns node with matching prefix
            (2) node.add( suff ) # adds telescoping branch under node.arr """
        try: #empty suff raises IxErr which happens for search(duplicate_string)
            newnode=TrNod(suff[0]) #empty str raises IxErr
            self.arr.append(newnode)
            self.arr.sort()
            if(suff[1:]):
                newnode.add(suff[1:]) #else we've added chars all the way to final $
        except IndexError:
            pass
    def tos(s,string_buffer,indent=0):
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
        print(self.__sizeof__())
    def insert(s,inp=[]):
        """User-friendly bulk wrapper for search() and add().
        Duplicate strings are silently ignored.
        Terminal '$' on inputs will be added.
        Call as: root_node.insert(['mystring','someother'])  """
        for elem in inp:
            suff,node=s.search(elem+'$')
            node.add(suff)
    def delstr(s,inp=[]):
        """User-friendly wrapper for bulk search() and delete() 
        No terminal '$' on input.
        Missing strings are silently ignored.
        Call as: root_node.delstr(['mystring','someother'])"""
        for elem in inp:
            suff,node=s.search(elem[:-1])
            node.delete()

# always need to make a root, init the cache with it
#help(TrNod)
a=TrNod('')
TrNod.init_cache()
print('root node is: '+str(a))
suff,node=a.search('bc$')
node.add(suff)
a.dump()
print('\nsrc(bc$) + add() returns --> suff,node '+str(suff)+','+str(node.ch))
a.dump()
suff,node=a.search('bc$')
node.add(suff)
print('\nsrc(bc$) +add () returns --> suff,node '+str(suff)+','+str(node.ch))
a.dump()
suff,node=a.search_memo('bck$')
node.add(suff)
print('\nsrc_memo(bck$) +add() returns --> suff,node '+str(suff)+','+str(node.ch))
a.dump()
print("\n---cache.ch's---")
TrNod.cache.dump()
print('-----')
suff,node=a.search_memo('bd$')
node.add(suff)
print('\nsrc_mem(bd$) returns --> suff,node '+str(suff)+','+str(node.ch))
a.dump()
print("\n---cache.ch's---")
TrNod.cache.dump()
print('-----')
suff,node=a.search('bd$')
node.add(suff)
print('\nsrch(bd$) returns --> suff,node '+str(suff)+','+str(node.ch))
a.dump()
print("\n---cache.ch's---")
TrNod.cache.dump()
print('-----')
