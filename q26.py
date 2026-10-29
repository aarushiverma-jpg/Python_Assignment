sentence="Python is easyyyyy"

lis=sentence.split()
d={}

for word in lis:
    d[word]=len(word)

max=0
for key,value in d.items():
    if max<value:
        max=value
        max_key=key

print(f"Longest word is {max_key}")