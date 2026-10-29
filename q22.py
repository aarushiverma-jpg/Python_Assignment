s="dfghgfdsdfghgfdfdfff"

d={}
for ch in s:
    d[ch]=d.get(ch,0)+1

max=0
max_key=None
max2=0
max2_key=None

for key in d.keys():
    if d[key]>max:
        max2=max
        max2_key=max_key
        max=d[key]
        max_key=key
    elif max2>d[key]>max:
        max2=d[key]
        max2_key=key

print(f"Second most frequent letter is {max2_key}")