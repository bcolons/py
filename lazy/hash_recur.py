def hash_recur(obj,flat_arr=[]): #shared
    '''Traverse down nested objects creating a single flat list of members (FIXME plus some None's)'''
    try: # is dict?   
        for each in obj.keys(): # raises AttributeError if not dict
                flat_arr.append(hash_recur(each,flat_arr))
                flat_arr.append(hash_recur(obj[each],flat_arr))
    except AttributeError: # not a dict
        try: # is str? return it, is_iterable recur...
            if obj == str:
                return obj
            else:
                for each in obj: # raises TypeError if not iterable
                    flat_arr.append(hash_recur(each,flat_arr))
        except TypeError: # is a non-str primitive, terminate recursion
            if obj != None:
                return obj

flat=[]
s='1'
hash_recur(d:=[(1,None,3,4,5,{ True ,False}),{1:11,2:{22:222,33:333}}],flat)
hash_recur(d:=[(1,None,3,4,5,{ True ,False}),{1,11,2,{22,222,33,333}}],flat)
print(flat)
for each in s:
    print(each)
    
