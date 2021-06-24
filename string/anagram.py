def anagram(l):
    hash={}
    for i in l:
        k="".join(sorted(i))
        if k in hash:
            hash[k].append(i)
        else:
            hash[k]=[i]
    ans=[]
    for i in hash:
        ans.append(hash[i])
    return ans
print(anagram(["yo","act","flop","tac","foo","cat","oy","olfp"]))
