s="aarushi"
li=list(s)
l=0
r=len(li)-1
while l<r:
    li[l],li[r]=li[r],li[l]
    l+=1
    r-=1
s="".join(li)
print(f"Reverse string is {s}")