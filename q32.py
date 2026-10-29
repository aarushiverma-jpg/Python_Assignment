s="aadaa"
l=0
r=max=1
i=j=0
while l<r<len(s) :
    lis=list(s[l:r+1])
    l1=0
    r1=len(lis)-1
    while l1<r1:
        lis[l1],lis[r1]=lis[r1],lis[l1]
        l1+=1
        r1-=1
    reverse="".join(lis)
    if reverse==s[l:r+1]:
        if max<r-l+1:
            max=r-l+1
            i=l
            j=r
        r+=1
    elif r<=len(s)-1:
        r+=1
    else:
        l+1

print(f"Longest palindrome sub string is {s[i:j+1]} and length is {max}")