n=int(input("Enter the size of array:"))
print("Enter an array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)
print("After swapping first and last number:")
temp=a[0]
a[0]=a[-1]
a[-1]=temp
print(a)