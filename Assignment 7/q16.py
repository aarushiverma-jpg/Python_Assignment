str="hello"
d={}

for s in str:
    if s in d:
        d[s]+=1
    else:
        d[s]=1
print("Frequency of each character in a string:")
print(d)