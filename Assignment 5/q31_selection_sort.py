n=int(input("Enter the size of array:"))
print("Enter the array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

print("Sorted array by selection sort algorithm:")
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if a[j]<a[min]:
            min=j
    a[i],a[min]=a[min],a[i]

print(a)
