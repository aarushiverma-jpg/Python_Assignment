n=int(input("Enter the size of array:"))
print("Enter an array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

max=a[0]
min=a[0]

for i in range(1,n):
    if a[i]>max:
        max=a[i]
    elif a[i]<min:
        min=a[i]

print(f"minimum is {min} and maximum is {max}")