l=["cat", "apple", "dog", "mango"]
d={len(i):[] for i in l}

for s in l:
    d[len(s)].append(s)
print("Group of words by their length:")
print(d)