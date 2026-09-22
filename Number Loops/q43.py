n=int(input("Enter a number:"))
sum=0
i=0
while n:
    r=n%10
    sum=sum+r*(2**i)
    i+=1
    n//=10
print("Binary is ",sum)