sentence="Python is easy"

lis=sentence.split()

for i in range(len(lis)):
    s=list(lis[i])
    l=0
    r=len(s)-1
    while l<r:
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1
    lis[i]="".join(s)

sentence=" ".join(lis)
print(sentence)