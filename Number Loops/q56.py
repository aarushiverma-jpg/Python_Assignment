n=int(input("Enter 1st number:"))
m=int(input("Enter 2nd number:"))
for i in range (n+1,m):
    fact=1
    temp=i
    while i!=0:
        fact=fact*i
        i=i-1
    print(f"Factorial of {temp} is {fact}")
