n=int(input("Enter a number:"))
sum=0
temp=n
while n:
    r=n%10
    fact=1
    while r!=1:
        fact=fact*r
        r=r-1
    sum=sum+fact
    n=n//10
if temp==sum:
    print("strong")
else:
    print("not strong")