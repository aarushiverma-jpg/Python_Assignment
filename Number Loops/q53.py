n=int(input("Enter 1st number:"))
m=int(input("Enter 2nd number:"))
print("Strong numbers are:",end=" ")
for i in range (n+1,m):
    sum=0
    temp=i
    while i:
        r=i%10
        fact=1
        while r>0:
            fact=fact*r
            r=r-1
        sum=sum+fact
        i=i//10
    if temp==sum:
        print(temp,end=" ")
