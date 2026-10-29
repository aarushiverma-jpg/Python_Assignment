def max_frequent(s):
    d={}

    for ch in s:
        d[ch]=d.get(ch,0)+1

    max=0
    max_key=None

    for key in d.keys():
        if d[key]>max:
            max=d[key]
            max_key=key
    return max,max_key

s="dfghgfdsdfghgfdfdfff"
max,key=max_frequent(s)
print(f"Most frequent letter is {key}")