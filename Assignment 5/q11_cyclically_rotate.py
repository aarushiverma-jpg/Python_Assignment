n=int(input("Enter the size of array:"))
print("Enter the array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

k=int(input("Enter times to rotate: "))

print("Cyclically rotated array: ")
for _ in range(k):
    temp=a[0]
    for i in range(n-1):
        a[i]=a[i+1]
    a[n-1]=temp

print(a)
