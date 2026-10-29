def str_to_dict(s):
    d={}
    for ch in s:
        d[ch]=d.get(ch,0)+1
    return d

s="programming"
d=str_to_dict(s)
print(d)