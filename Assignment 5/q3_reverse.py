n=int(input("Enter the size of array:"))
print("Enter an array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

print("Reverse of a array is:",end=" ")
l=0
r=n-1
while(r>l):
    a[l],a[r]=a[r],a[l]
    l+=1
    r-=1
print(a)