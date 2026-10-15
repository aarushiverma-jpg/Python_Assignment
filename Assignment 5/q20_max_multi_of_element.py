n=int(input("Enter the size of array:"))
print("Enter an array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

max=a[0]
print("Max multiplication of elements: ")

for i in range(n):
    cs=1
    for j in range(i,n):
        cs=a[j]*cs
        if cs>max:
            max=cs

print(max)