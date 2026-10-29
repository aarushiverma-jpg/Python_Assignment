def reverse(s):
    lis=list(s)
    l=0
    r=len(lis)-1
    while l<r:
        lis[l],lis[r]=lis[r],lis[l]
        l+=1
        r-=1
    return "".join(lis)

def longest_palindrome(s):
    l=0
    r=max=1
    i=j=0
    while l<r<len(s) :
        re=reverse(s[l:r+1])
        if re==s[l:r+1]:
            if max<r-l+1:
                max=r-l+1
                i=l
                j=r
            r+=1
        elif r<=len(s)-1:
            r+=1
        else:
            l+1
    return i,j,max

s="aada"
start,stop,max=longest_palindrome(s)
print(f"Longest palindrome sub string is {s[start:stop+1]} and length is {max}")