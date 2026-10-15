n=int(input("Enter the size of array:"))
print("Enter the array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

print("Sorted array by insertion sort:")
for i in range(1,n):
    temp=a[i]
    j=i-1
    while j>=0 and a[j]>temp:
        a[j+1]=a[j]
        j-=1
    a[j+1]=temp

print(a)