def star_func(posarg='ignored below',/,*star):
    for arg in star:
        print(arg)
star_func('a','b','c')
def sstar_func(**star):
    for arg in star:
        print(arg, star[arg])
sstar_func(hey='dud',what='evah')
def double_star_func(*args,*, **star):
    for arg in star:
        print(arg, star[arg])
sstar_func('asdf',/,hey='dud',what='evah')
# func sigs obey (pos_onl1, pos_onl2,/, kw_or_pos1=key1, *, kw_onl2=key2, *star_wild_arr_of_non_kw, **dict_of_keywords_and_vals)
