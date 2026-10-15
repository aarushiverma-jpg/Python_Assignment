n=int(input("Enter the size of array:"))
print("Enter an array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

print("Sorted array of 0s,1s and 2s:")
l=0
m=0
h=n-1

while(m<=h):
    if a[m]==0:
        a[l],a[m]=a[m],a[l]
        l+=1
        m+=1
    elif a[m]==1:
        m+=1
    else:
        a[h],a[m]=a[m],a[h]
        h-=1

print(a)