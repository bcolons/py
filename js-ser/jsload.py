from json import load
import sys
class EngWords:

    def __init__(s):
        s.inp =''
    def open_read_word_list(s,word_list_file):
        with open(word_list_file,'r') as fs:
            s.inp=load(fs)
        sw=set(s.inp)
ew=EngWords()
ew.open_read_word_list( sys.argv[1])
