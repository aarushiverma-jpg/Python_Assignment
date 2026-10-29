s="dfghgfdsdfghgfdfdfff"

d={}
for ch in s:
    d[ch]=d.get(ch,0)+1

max=0
max_key=None

for key in d.keys():
    if d[key]>max:
        max=d[key]
        max_key=key

print(f"Most frequent letter is {max_key}")