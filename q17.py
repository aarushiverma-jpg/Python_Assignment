s="abcdanfbcd"

d={}
for ch in s:
    d[ch]=d.get(ch,0)+1

for key in d.keys():
    if d[key]==1:
        print(f"First not repeating letter is {key}")
        break