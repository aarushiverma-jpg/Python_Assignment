n=int(input("Enter the size of array:"))
print("Enter an array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

max=a[0]
sum=[0]*(n+1)
print("Max sum of elements: ")

for i in range(n):
    sum[i+1]=sum[i]+a[i]
for i in range(n):
    for j in range(i+1,n+1):
        cs=sum[j]-sum[i]
        if cs>max:
            max=cs

print(max)