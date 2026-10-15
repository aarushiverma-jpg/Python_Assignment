m=int(input("Enter the size of array:"))
print("Enter the array:")
a=[]
for _ in range(m):
    i =int(input())
    a.append(i)

flag=True
result=[]
pos=[i for i in a if i>0]
neg=[i for i in a if i<0]
count_zero=m-(len(pos)+len(neg))
p=0
n=0

for i in range(len(pos)+len(neg)):
    if flag and p<len(pos):
        result.append(pos[p])
        p+=1
        if n<len(neg):
            flag=False
    elif not flag and n<len(neg) :
        result.append(neg[n])
        n+=1
        if p<len(pos):
            flag=True

while count_zero:
    result.append(0)
    count_zero-=1

print(result)