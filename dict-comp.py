arr = 1,2,3,4,5
myd = {a*100: a*10 for a in arr} # dict comprehension!
#for key in iter(myd):
for key in myd:
    print(key,myd[key])
