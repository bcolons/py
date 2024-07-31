class TrNod:
    cache=[] # in order sequence of TrNod's with the prior searched string's matching prefix nodes 
    # search_memo()-cache_suff() not threadsafe, 
    # must lock incoherent cache between search_memo()-truncate and return of cach_suff() after completed update
    def __init__(s,ch=''):
        s.ch=ch
        s.arr=[]
    def __lt__(s,t):
        """Each TrNod list is kept in alphabetical order for a (not_implemented) mergesort-style logN-time search """
        return s.ch < t.ch
    def init_cache(root_node):
        """Initialize search_memo()'s prior TrNod list (the 'cache tree' ) as TrNod.cache=[root_node]"""
        TrNod.cache.append(root_node)
    def dump_cache(self):
        """Print each TrNod.cache[elem].ch"""
        print('cache: ',end='')
        for elem in TrNod.cache[1:]:
            print(elem.ch+' ',end='')
        print()
    def chsearch(self,inp):
        """Check the first char of inp for a match in a single ('child node') TrNod.arr
        Returns first matched child TrNod ref or else False
        To get a matching child TrNod (or False) for inp[0] call as:
            childTN = node.chsearch(inp) """
        for child in iter(self.arr):
            if child.ch==inp[0]:
                return child # first char matched this child TrNod
        return False
        
    def search_memo(self,suff): # try for a closer to linear search for spatial/temporal -ly local (a-z sorted) inputs
        """earlier search_mempy()..."""
        ix=0 # == TrNod.cache.index(TrNod('')) ie the root node, this index will trim cache after the last hit
        elem=TrNod.cache[0]
        for elem in iter(TrNod.cache[1:]): # '' is initial / root char in cache, input string never has this. Also indexes are aligned btwn suff and TrNod.cache[1:]
            if(suff[ix]==elem.ch): # if( first node in cache == first char in string ) -> cache hit
                ix+=1 # if we trim now slice is TrNod.cache[:ix]
            else: # remaining novel suffix is delegated to recursive cache_suff 
                break
        TrNod.cache=TrNod.cache[:ix+1] #truncate the cache to the matching prefix just before miss, TrNod.cache index is one higher than suff[ix]
        return elem.cache_suff(suff[ix:]) # jump across to characterwise main_tree.search(), to facilitate charwise caching; returns final return of search()
    def search_mempy(self,suff):
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
        ix=0
        elem=TrNod.cache[0]
        for elem in iter(TrNod.cache[1:]):
            if(suff[ix]!=elem.ch):
                break
            else:
                ix+=1
        TrNod.cache=TrNod.cache[:ix]
        return elem.cache_suff(suff[ix:])
    def cache_suff(self,suff):
        """
        Updates the suffix of TrNod.cache with remaining TrNod refs in a loop via:
            Characterwise search() in tree, TrNod.cache.append( each matched TrNod )
            Returns last matching (node,suff) ie. same return case/vals as search() and search_memo()"""
        if(not suff): # return if last_call( suff[1:] ) is []   ...whole suff matched main tree (slices dont raise IxErr's)
            return (self,suff)
        node,suff_ignore=self.search(suff[0]) #suff_ignore is always None because suff[0] is a single elem
        if(node.ch!=suff[0]): # return if suffix has a main-tree-novel (nonmatch) char 
            return (self,suff)
        else: # go deeper! 
            TrNod.cache.append(node) # add matching child TrNod to cache
            return node.cache_suff(suff[1:]) # recurse to check next char against main tree node...
            
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

    def add_mempy(self, suff):
        """Equivalent to add() although updates cache with novel suffix.
        Simply add each add()'d TrNod to the cache array Ǝ ∴ """ 
        if(suff): #suff [] can happen if for search(duplicate_str)...don't do anything
            newnode=TrNod(suff[0])
            self.arr.append(newnode)
            TrNod.cache.append(newnode)
            if(suff[1:]):
                newnode.add(suff[1:])
            
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
            string_buffer=[""]
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

# always need to make a root, init the cache with it
#help(TrNod)
a=TrNod('')
a.init_cache()
#print('root node is: '+str(a))

node,suff=a.search('bc$')
print('sm bc$')
a.dump()
a.dump_cache()
print('ad bc$')
node.add(suff)
a.dump()
a.dump_cache()
print('sm bc$')
node,suff=a.search_memo('bc$')
a.dump_cache()
print('ad bc$')
node.add(suff)
a.dump()
a.dump_cache()
print('sm bck$')
node,suff=a.search_memo('bck$')
a.dump_cache()
print('ad bck$')
node.add(suff)
a.dump()
a.dump_cache()
print('sm bd$')
node,suff=a.search_memo('bd$')
a.dump_cache()
print('ad bd$')
node.add(suff)
a.dump()
a.dump_cache()
print('sm bckale$')
node,suff=a.search_memo('bckale$')
a.dump_cache()
print('ad bckale$')
node.add(suff)
a.dump()
a.dump_cache()
print('sm bckaleohz$')
node,suff=a.search_memo('bckaleohz$')
a.dump_cache()
print('ad bckaleohz$')
node.add(suff)
a.dump()
a.dump_cache()
print("\n---final cache.ch's---")
for elem in iter(a.cache):
    print(elem.ch +' ',end='')
print('-----')
