import typing
def hash_recur(obj,flat_arr=[]): #shared
    '''Traverse down nested objects creating a single flat list of members (FIXME plus some None's)'''
    if isinstance(obj,str | int|float|None|bool):
        return obj
    elif isinstance(obj , dict):
        for each in obj.keys(): # raises AttributeError if not dict
                flat_arr.append(hash_recur(each,flat_arr))
                flat_arr.append(hash_recur(obj[each],flat_arr))
    else: #if isinstance(obj,iter): # bc_dnw iterable not a type
        try: 
             for each in obj: # raises TypeError if not iterable
                flat_arr.append(hash_recur(each,flat_arr))
        except TypeError as t: #  wtf...
            print(t, 'type missed...')
class hlist(list):
    def __hash__(s):
        tot=1
        for each in s:
            if each != None: tot+=1
        return tot

class hset(set):
    def __hash__(s):
        tot=1
        for each in s:
            if each != None: tot+=1
        return tot

flat=[]
s='1'
hash_recur(d:=[(1,None,(3,4),5,{(2,3), True ,False}),{1:11,2:{22:222,33:333}}],flat)
hash_recur(d:=[(1,None,3,4,5,{ True ,False}),{1,11,2,hset({22,222,33,333})}],flat)
print(flat)
print(d)
#print(hset({1,2,3,{4,5,6}}))
print(hash_recur(hset({1,2,3, hset({4,5,6})})))
print(hset({1,2,3, hset({4,5,6})}))
print(hash(hset({1,2,3, hset({4,5,6})})))
    
