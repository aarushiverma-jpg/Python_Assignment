n=int(input("Enter the size of array:"))
print("Enter the array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)
k=int(input("Enter the k(target):"))
count=0
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]+a[j]==k:
            count+=1

print(f"The pairs are {count}")