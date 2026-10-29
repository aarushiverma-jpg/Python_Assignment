def first_not_repeating(s):
    d={}
    for ch in s:
        d[ch]=d.get(ch,0)+1

    for key in d.keys():
        if d[key]==1:
            return key

s="abcdanfbcd"
key=first_not_repeating(s)
print(f"First not repeating letter is {key}")
