def common_prefix(lis):
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
    return word

lis=["flower", "flow", "floght"]
word=common_prefix(lis)
print(f"Longest common prefix is {word}")