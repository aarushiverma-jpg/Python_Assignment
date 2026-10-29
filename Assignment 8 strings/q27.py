sentence="She is soooo confidenttt"
d={}

for ch in sentence:
    key=ch.lower()
    d[key]=d.get(key,0)+1

print("Duplicate Values are:")

for key,value in d.items():
    if value>1:
        print(f"'{key}'-->{value}")