n=int(input("Enter a number:"))
sum=1
i=2
print("1 ",end="")
while n:
    sum=sum+(1/i)
    print(f" + 1/{i}",end="")
    i=i+1
    n=n-1
print(f"\nsum is {sum:.2f}")