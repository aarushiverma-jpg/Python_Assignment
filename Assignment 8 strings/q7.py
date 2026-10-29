s="ftegyu09oVBH"
lis=list(s)
for i in range(len(lis)):
    if 97<=ord(lis[i])<=122:
        lis[i]=chr(ord(lis[i])-32)

upper="".join(lis)
print(f"Upper case of {s} is {upper}")