class SrNod:
    def __init__(s,ch=''):
        s.ch=ch
        s.arr=[]
    def chsearch(self,inp):
        """Check the first char of inp for a match in a single SrNod.arr
        Returns first matched child SortedNod ref or else False"""
        for child in iter(self.arr):
            if child.ch==inp[0]:
                return child # first char matched this child SrNod
        return False
        
    def search(self,suff): 
        """ Searches recursively for a string/prefix match and returns last matching character node in tree.
        Returns: ( 
                   suff,       # remaining char suffix past last matching char
                   node        # SrNod ref for last matched prefix char
                 )

        Call with $ input string terminator (" inp$ ") except to delete() (...a terminating $ node  use " inp_no$ ")

        To spellcheck a string, call as root_node.search( inp$ ) 
        A full match will return 
            ( '' , a SrNod_ref with self.ch=='$' ) 
        An input which fully matches a tree prefix will return 
            ( '' , a SrNod_ref with self.ch=='last_matching_prefix_char' ) 
        An input which has a matching prefix and a unique suffixe will return 
            ( 'uniq_suff' , a SrNod_ref with self.ch=='last_matching_prefix_char' ) 

        Use input and return values to add and delete words from tree as follows:

        add() - call as root_node.search( inp$ ) 
            not all initial chars of inp$ can match (duplicate to existing string)
            node.add( mchar_suff ) adds telescoping branch under node.arr

        delete() - call as root_node.search( inp_no$ ) to get parentnode.arr 
            node.delete() will delete terminal SrNod('$') leaving a potentially valid (or not) 
            prefix to other (or no) existing $ terminated words---valid words always have final $, 
            though the tree is not required to have $-leaves/terminals (tree may have orphan prefixes) """
        if(not suff): # must have matched all the way to end of input
            # if terminal $ was stripped, caller may now self.delete() which calls self.arr.remove(SrNod('$'))
            return (suff,self) #suff is False here, out of suffix characters
        child=self.chsearch(suff) # try find a match child node for initial remaining char at this level
        if(not child): # False means no matching chars at this level, 
            #caller may now self.add(suff) to go under self.arr
            return (suff,self)
        else: 
            return child.search(suff[1:]) # recurse w rest of word and child SrNod

    def delete(self): 
        """Demote a string from valid to invalid by deleting terminal $ node from tree
        Caller must strip terminal $ to find parent of terminal $ ie search( inp_no$ )"""
        term_dollar_node=self.chsearch('$')
        try:
            self.arr.remove(term_dollar_node) #gc does the rest
        except ValueError:
            pass #remove() tried to delete something which doesnt exist

    def add(self, suff): 
        """ Recursive/telescoping single-initial-char insert method
        Prior mchar_suff,node= search( inp$ ) returns node with matching prefix for node.add( mchar_suff ) here """
        try: #empty suff raises IxErr which happens for search(duplicate_string)
            newnode=SrNod(suff[0]) #empty str raises IxErr
            self.arr.append(newnode)
            if(suff[1:]):
                newnode.add(suff[1:]) #else we've added chars all the way to final $
        except IndexError:
            pass
    def tos(s,sb,indent=0):
        """Recursively to-string the entire SrNod tree characters with dot-indent to show depth level."""
        sb+=s.ch
        if(s.arr):
            indent+=1
            sb+="<"+'.'*indent
            for child in iter(s.arr):
                child.tos(sb,indent)
            sb+="."*indent+">"
        return str(sb)
    def dump(s,sb=None):
        """Print entire tree; flat list from root_node.tos() is printed without commas, quotes or newlines."""
        if(sb==None):
            sb=["\n"]
        a.tos(sb)
        for elem in sb:
            print(elem,end='')
    def insert(s,inp):
        """User-friendly wrapper for search() and add().
        Call as root_node.insert('mystring')---terminal '$' on input will be added
        Duplicate strings are silently ignored."""
        suff,node=s.search(inp+'$')
        node.add(suff)

    def delstr(s,inp):
        """User-friendly wrapper for search() and delete() (no terminal '$' on input).
        Call as root_node.remove('mystring')
        Missing strings are silently ignored."""
        suff,node=s.search(inp[:-1])
        node.delete()

a=SrNod('')

suff,node=a.search('bc$')
node.add(suff)
a.insert('bcy')
a.insert('bcy')
a.delstr('bcy')
a.delstr('bcy')
suff,node=a.search('bck$')
node.add(suff)
suff,node=a.search('bckqwer$')
print('suff: '+str(suff)+', root: '+str(a)+', matchednode: '+str(node.ch))
node.add(suff)
suff,node=a.search('bcj$')
node.add(suff)
a.dump()
suff,node=a.search('bcj')
node.delete()
a.dump()
