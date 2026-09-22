n=int(input("Enter 1st number:"))
m=int(input("Enter 2nd number:"))
print("Odd numbers are:",end=" ")
for i in range (n+1,m):
    if i%2==1:
        print(i,end=" ")