class ChNod:
    """
    Description:
    Node in a 26-tree of characters. 
    Each character at n-levels deep corresponds to the nth character in a stored word.
    __str__() returns a single char.
    genstr(string buffer) returns the entire tree formatted as nested arrays
    genbranch('',string[]) returns arr of all branches (ie. the set of stored words )
    Dollar sign terminates a word.

    Implementation:
    Each word is characterwise inserted into a tree of ChNod's.
    Each ChNod has a array of next possible character-ChNod's.

    Example:
    words: hell, hello, hello world, helium are represented as (actual refs not shown):
    ['h',['e',['l',['l','i',['$','o','u',['$',' ','m',['w','$',['o',['r',['l',['d',['$']]]]]]]]]]]]
    """
    iden=0

    def __init__(s,ch):
        """A ChNod must have a character and a possibly empty list of child ChNod's."""
        s.arr=[]
        s.ch=ch
#        print(str(s.__dict__))
    def genstr(s,stbuf=[''],ct=0):
        """Output entire tree as a flat string of paren-nested characters with call trace counter.
        Use prar to strip quotes and commas."""
        stbuf[-1]+='('
        stbuf[-1]+=str(s.ch) # we went down one level when called
        for elem in s.arr:
            ct+=1
            ChNod.iden+=1
    #        print('ct= '+str(ct))
    #        print('X' * ChNod.iden +'elem.genstr(stbuf,ct)'+str(strbuf)+' , '+str(ct))
            elem.genstr(stbuf,ct) # we push down one level
            stbuf[-1]+=")" # we pop'd back up one level to get here
            ChNod.iden-=1
        return stbuf
    def genstr_noct(s,stbuf=[]):
        """Output entire tree as a flat string of paren-nested characters.
        Use prar to strip quotes and commas."""
        stbuf.append("("+str(s.ch)) # we went down one level when 
        for elem in s.arr:
            elem.genstr(stbuf) # we push down one level
            stbuf.append(")") # we pop'd back up one level to get here
        return stbuf
    def chcontains(s,inp): # checks if child arr contains char, used for U in crud
        """Returns True if input character matches any ChNod.arr ChNod's and False otherwise"""
        for child in s.arr:
            if child.ch==inp:
                return True
        return False
    def chindex(s,inp): # checks if child arr contains char, used for C or U in crud
        """Check for an input character match in any ChNod.arr of ChNod's  
        Returns index of match or -1 if no match"""
        i=-1
        for child in s.arr:
            i+=1
            if child.ch==inp:
                return i #caller will recurse with this indexed ChNod and inp[1:]
        return -1
        
    def __str__(s):
        return s.ch
    def genbran_try(s,pre,branches): 
        """try-except implementation of genbran()
        Output dump of entire tree"""
        i=iter(s.arr)
        while True: # sideways iteration
            try:
                elem=next(i) # raises StopIter if arr==[] or off end of arr 
                elem.genbran_try(pre+s.ch,branches) # push downward attempt foreach in ChNod[]
            except StopIteration: # sideways iteration reached end
                if(s.ch=='$'): # output actual terminated strings, not prefix fragments
                    branches.append(pre)
                break
        return branches
    def genbran(s,pre,branches): # much more readable and concise than genbran_try()
        """Generate a list with all strings in a ChNod tree
        Output dump of entire tree"""
        for elem in s.arr:
            elem.genbran(pre+s.ch,branches)
#   d           h
#  /| \        /| \
# / |  \      / |  \
#a  b   c    e  f   g
# genstr gives:
#inpoot=  ['',['d',['a',['$]],['b',['$']],['c',['$]]],'h',['d',['$']],'[e',['$']],['f',['$']]]]]
# genbranch gives: [ida, idb, idc, ihe, ihf, ihg]
# i
# |
# d --------------h
# |               |
# a -- b -- c     e -- f -- g
#Example: search(inp='dbz$',lastMIndex=-1,lastMCN=ChNod('')) 
    def search(s,inp,charix=-1):
        """ Returns tuple of (index of last matched input char, last matched ChNod)
        Used  for C or U  in crud for words in tree  Create/write/insert, Read/select, Update/write, Delete/write)
        If ...  
            a. input_string[output[0]]== '$' 
                and/or 
            b. output[1].ch=='$' 
                ....word is in tree, 
        (either a. or b. is sufficient, both are returned in order to insert the non-matching suffix of the string via ins())

        If a prefix of input_string exists in tree: 
            input_string[output[0]] and output[1] point to the last matching char and ChNod, respectively.

        If input_string and tree have no common prefix:
             output[0] == -1/ and output[1] == ChNod('') or root

        The three implemented cases:
        If not inp: 
            return last charix,selfref of last match eg. the prior recursive call
        matchCNix=s.chindex([inp[0]) # search in child array for char, save index
        If matchCNix, == -1 # non-match in child arr
            return prior charix,selfref # use this in ins(inp[charix+1:],s)
        Else 
            return search(inp[1:],charix+1) # increment input arr and charix and recurse
        """ 

        if(not inp):
            return ( charix, s)
        ch_inp=inp[0]
        ch_CNix=s.chindex(ch_inp)
        if(ch_CNix==-1):
            return ( charix, s)
        else:
            return s.arr[ch_CNix].search(inp[1:],charix+1) #recurse with rest of word and charix to next char

    def arbfun(s,func):
        func(s)

    #def arbsearch(s,inp,charix=-1,arbfun=lambda fs:print(str((fs.__dict__)))):
    def arbsearch(s,inp,charix=-1,arbfun=lambda: ''):
        if(not inp):
            return ( charix, s)
        ch_inp=inp[0]
        #s.arbfun(lambda fs: print(str( fs.__dict__))) #call arbitrary_function(self) f/e ChNod traversed
        def  innfun(s):
            print(str( s.__dict__))
        innfun(s)
        #arbfun(s) #call arbitrary_function(self) f/e ChNod traversed
        ch_CNix=s.chindex(ch_inp)
        if(ch_CNix==-1):
            return ( charix, s)
        else:
            return s.arr[ch_CNix].arbsearch(inp[1:],charix+1) #recurse with rest of word and charix to next char

    def ins(s, inp,matched=False):
        """Insert unique input suffix after searching for any matching prefix.
        Test for successful insertion of '$' terminated inputs with exists(input_str).
        """
        if(not matched): # first we get rid of the matching prefix and return the last matching char ix and matching ChNod
            charix,matchingCN=s.search(inp) 
            matchingCN.ins(inp[charix+1:],True) # recurse, this time with the non-matching suffix to add to matching node.arr
        else:
            newCN=ChNod(inp[0]) #create next new ChNod (don't call ins with empty string, will raise IndexError)
            s.arr.append(newCN) # append it to self.arr
            if(inp[1:]): # end of word test, if so return
                newCN.ins(inp[1:], True)
    def exists(s,inp):
        """
        Test for successful insertion of '$' terminated input with exists(input_str).
        """
        charix,matchingCN=s.arbsearch(inp)
        return inp[charix]=='$'

if(__name__=='__main__'):
    z=ChNod('$')
    a=ChNod('a')
    a.arr=[z]
    b=ChNod('b')
    b.arr=[z]
    c=ChNod('c')
    c.arr=[z]
    d=ChNod('d')
    e=ChNod('e')
    e.arr=[z]
    f=ChNod('f')
    f.arr=[z]
    g=ChNod('g')
    g.arr=[z]
    h=ChNod('h')
    i=ChNod('')
    d.arr =[a,b,c]
    h.arr=[e,f,g]
    i.arr=[d,h]
    #z.arr=[i]
    #
    strbuf=['']
    print(str(i.genstr(strbuf)))
    strbuf=['']
    print('----')
    inp=['dathigh$','qqqqq','funny','looking','dogboy','shazam']
    for each in inp:
        i.ins(each)
    print(str(i.genstr(strbuf)))
    #print(str(i.__dict__))
