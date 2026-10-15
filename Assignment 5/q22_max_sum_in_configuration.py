n=int(input("Enter the size of array:"))
print("Enter an array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

print("Max sun in configuration:",end=" ")
max_len=0
for _ in range(n):
    sum=0
    for i in range(n):
        sum+=(a[i]*i)
    if max_len<sum:
        max_len=sum
    temp=a[0]
    for i in range(n-1):
        a[i]=a[i+1]
    a[n-1]=temp

print(max_len)