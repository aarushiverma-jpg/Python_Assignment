n=int(input("Enter the size of array:"))
print("Enter the array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

print("longest consecutive sequence: ")
s=set(a)
max=0

for i in s:
    if i-1 not in s:
        length=1
        num=i
        while num+1 in s:
            length+=1
            num+=1
        if length>max:
            max=length

print(max)
 