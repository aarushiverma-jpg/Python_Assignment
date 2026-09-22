n = int(input("Enter a number:"))
print("Factors are:",end="")
for i in range (2,n//2+1):
    if n%i==0:
        print(i,end=" ")    