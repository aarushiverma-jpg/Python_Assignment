n = int(input("Enter a number:"))
i=2
while i<=n//2:
    if n%i==0:
        break
    i=i+1
if i>n//2 and n>1:
    print("prime")
else:
    print("not prime")