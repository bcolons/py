#!/usr/bin/env python3
import sys,re 
from ChNod import ChNod
from json import load
class ChNodioWrapper:
    """
    Populate a ChNod tree with whitespace delimited strings from a file.
    Each string is a word in a spellcheck dictionary which may be validated as follows.
        ChNod_instance.search(string) 
    Returns a tuple (last_matching_input_char, last_matching_ChNod) with a '$'.
    Either or both position(s) denote a match:
        ('$', this_ChNod_ref.ch=='$' )
    """
    def __init__(s):
        s.root=ChNod('')
        s.whitesp_pat = re.compile('[\s]')
        s.inp=''
    def populate(s): # C in crud, appends term '$' calls myChNod.ins(), uses cur myChNod.inp
        try:
            arr=s.whitesp_pat.split(s.inp) #must be able to mutate s.inp
            for line in arr:
                if(line):
                    s.root.ins(line+'$')
        except TypeError:
            pass
    def validate(s): #returns arr of misspelled words ie. any s.inp+$ elems missing from tree
        borklist=[]
        try:
            arr=s.whitesp_pat.split(s.inp) #must be able to mutate inp, hence itsa member
            for line in arr:
                if(line):
                    resp=s.root.search(line+'$')
                    try:
                        print('inp string: '+str((line+'$')[(resp[0])]))
                        print('ChNod.ch: '+str(resp[1].ch))
                    except IndexError:
                        print('Ix Err: '+str(line)+' at position '+str(resp[0]))
                    if((line+'$')[resp[0]]!='$'):
                        borklist.append(line)
            return borklist
        except TypeError:
            pass

    def open_doc(s,doc): #dump an inp doc to s.inp for subsequent action: populate(), validate(), delete()
        with open(doc,'r') as fs:
            s.inp=fs.read()

    def open_json_word_list(s,word_list_file):
        with open(word_list_file,'r') as fs:
            s.inp=load(fs)
        sw=set(s.inp)
        print(sw)

if(__name__=='__main__'):
    myspellchecker=ChNodioWrapper()
    #myspellchecker.open_doc(sys.argv[1])
    myspellchecker.open_json_word_list(sys.argv[1]) #open_doc() also dumps list, todo cast to dict, populate(dict_vals #the actual words)
    myspellchecker.populate()
    myspellchecker.open_doc(sys.argv[2]) # doc to spellcheck
    print('misspelled words are: '+str(myspellchecker.validate()))
    #print('test dump of spell db: '+str(myspellchecker.root.genstr()))
        #print('elem: '+line)
    #with open(sys.argv[1],'a') as fs:
        #stuff=fs.write('blahaldf')
