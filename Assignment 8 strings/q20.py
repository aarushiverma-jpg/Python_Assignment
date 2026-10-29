s="programming"

d={}
for ch in s:
    d[ch]=d.get(ch,0)+1

unique="".join(d.keys())
print(f"All the Not repeating letters are {unique}")