n=int(input("Enter the size of array:"))
print("Enter an array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

target=0
cs=0
print("Sum of elements equal to 0 is on: ")

for i in range(n):
    cs=0
    for j in range(i,n):
        cs=cs+a[j]
        if cs==target:
            print(i,j)