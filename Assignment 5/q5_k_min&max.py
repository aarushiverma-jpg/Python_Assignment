n=int(input("Enter the size of array:"))
print("Enter an array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)
k=int(input("Enter the value of 'k':"))

for i in range(n-1):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]

k_min=a[k-1]
k_max=a[n-k]
print(f"minimum is {k_min} and maximum is {k_max}")