n=int(input("Enter the size of 1st array:"))
print("Enter the 1st array in descending order:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

m=int(input("Enter the size of 2nd array:"))
print("Enter the 2nd array in descending order:")
b=[]
for _ in range(m):
    i =int(input())
    b.append(i)

print("Merging both array in descending order is: ")
i=0
j=0
c=[]

while i<n and j<m:
    if a[i]>b[j]:
        c.append(a[i])
        i+=1
    elif b[j]>a[i]:
        c.append(b[j])
        j+=1
    else:
        c.append(a[i])
        i+=1
        j+=1

while i<n:
    c.append(a[i])
    i+=1

while j<m:
    c.append(b[j])
    j+=1

print(c)