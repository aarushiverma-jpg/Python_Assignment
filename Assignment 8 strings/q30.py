lis=["flower", "flow", "foght"]

word=""
f=True
i=0

while f:
    ch=(lis[0][i])
    for s in lis:
        if s[i]!=ch:
            f=False
            break
    else:
        word+=str(ch)
        i+=1

print(f"Longest common prefix is {word}")