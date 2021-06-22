def strng(one,o,two,tw,three,th):
    if th==len(three):
        return True
    s=three[th]
    fnl=False
    if o<len(one):
        if s==one[o]:
           fnl=strng(one,o+1,two,tw,three,th+1)
    if tw<len(two):
        if s==two[tw]:
           fnl=strng(one,o,two,tw+1,three,th+1)
    if o<len(one) and tw<len(two):       
        if s!=one[o] and s!=two[tw]:
           fnl=False
    return fnl
print(strng("abed",0,"cd",0,"abcdde",0))