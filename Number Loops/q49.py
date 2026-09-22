n=int(input("Enter 1st number:"))
m=int(input("Enter 2nd number:"))
print("Perfect numbers are:",end=" ")
for i in range (n+1,m):
    sum=0
    for j in range(1,i//2+1):
        if i%j==0:
            sum=j+sum
    if sum==i:
        print(f"{i}",end=" ")
