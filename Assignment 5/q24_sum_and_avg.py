n=int(input("Enter the size of array:"))
print("Enter an array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

sum=0
for i in range(n):
    sum+=a[i]
print(f"sum:{sum}\navg:{sum/n}")