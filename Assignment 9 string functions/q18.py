def first_repeating(s):
    d={}
    for ch in s:
        d[ch]=d.get(ch,0)+1

    for key in d.keys():
        if d[key]>1:
            return key
s="programming"
key=first_repeating(s)
print(f"First repeating letter is {key}")