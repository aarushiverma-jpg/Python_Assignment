n=int(input("Enter 1st number:"))
m=int(input("Enter 2nd number:"))
print("Armstrong numbers are:",end=" ")
for i in range (n+1,m):
    temp=i
    length=0
    sum=0
    while i:
        length=length+1
        i=i//10
    i=temp
    while i:
        r=i%10
        sum=sum+r**length
        i=i//10
    if sum==temp:
        print(temp,end=" ")