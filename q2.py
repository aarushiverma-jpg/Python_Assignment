s="amma"
li=list(s)
l=0
r=len(li)-1
while l<r:
    li[l],li[r]=li[r],li[l]
    l+=1
    r-=1
r="".join(li)

if r==s:
    print(f"{s} is Palindrome")
else:
    print(f"{s} is Not palindrome")