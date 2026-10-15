n=int(input("Enter the size of array:"))
print("Enter an array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

target=int(input("Enter the target:"))

print("Sum of elements equal to target is on: ",end=" ")

for i in range(n-1):
    for j in range(i+1,n):
        if (a[i]+a[j])==target:
            print (i,j)