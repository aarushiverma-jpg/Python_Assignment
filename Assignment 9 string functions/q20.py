def unique_ch(s):
    d={}
    for ch in s:
        d[ch]=d.get(ch,0)+1
    return "".join(d.keys())

s="programming"
unique=unique_ch(s)
print(f"All the Not repeating letters are {unique}")