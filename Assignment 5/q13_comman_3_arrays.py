n=int(input("Enter the size of 1st array:"))
print("Enter the 1st array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

m=int(input("Enter the size of 2nd array:"))
print("Enter the 2nd array:")
b=[]
for _ in range(m):
    i =int(input())
    b.append(i)

l=int(input("Enter the size of 3rd array:"))
print("Enter the 3rd array:")
c=[]
for _ in range(l):
    i =int(input())
    c.append(i)

intersection=[]

while i<n or j<m or k<l:
    if a[i]==b[j]==c[k]:
        intersection.append(a[i])
        i+=1
        j+=1
        k+=1
    elif a[i]<b[j]:
        i+=1
    elif b[j]<c[k]:
        j+=1
    else:
        k+=1

print(f"Comman number is {intersection}")