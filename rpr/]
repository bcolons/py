import json
class EngWords:
    def __init__(s):
        # js object is {"key":val} or {"key1":val1,"key2":val2, ..} same as dict (set not json serializable)
        # js array is [val1,val2, ..] same as list, tuple treated like (immut) list
        # js value is true/false/null float/int/"string" (also array or object)
        #...plust shit tons of whitespace

        s.stuff= {"a":"apple","b":"bed","c":["cot","cane","crabapple"],"d" : (1,2,3),"e":(4,5,6)}
        s.somedict= {"a":s.stuff,"b":"bed","c":("cot","cane","crapapple")}
        print(s.somedict)
    def dump_json_word_list(s,word_list_file):
        with open(word_list_file,'w') as fs:
            json.dump(s.somedict,fs,indent=92)
        #sw=set(s.inp)
ew=EngWords()
ew.dump_json_word_list('empty.js') #raises TypeError if not js serializable
print(ew.__dict__)
print(EngWords.__dict__)

