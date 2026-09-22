n=int(input("Enter a number:"))
length=0
temp=n
while n:
    length+=1
    n=n//10
print(F"{temp} is a {length} digit number")
