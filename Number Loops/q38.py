n=int(input("Enter a number:"))
temp=n
length=0
power=1
sum=0
while n:
    length+=1
    n=n//10
n=temp
while n:
    r=n%10
    power=1
    for _ in range(length):
        power=power*r
    sum=sum+power
    n=n//10
if sum==temp:
    print("Armstrong")
else:
    print("Not armstrong")