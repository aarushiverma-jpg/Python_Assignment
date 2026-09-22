n=int(input("Enter a 4 digit number:"))

r=n%10
print(r,end="")
n=n//10

r=n%10
print(r,end="")
n=n//10

r=n%10
print(r,end="")
n=n//10

r=n%10
print(r,end="")
n=n//10

if(n!=0):
    print("Invalid number.")