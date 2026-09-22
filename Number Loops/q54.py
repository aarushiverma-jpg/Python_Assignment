n=int(input("Enter 1st number:"))
m=int(input("Enter 2nd number:"))
print("Even numbers are:",end=" ")
for i in range (n+1,m):
    if i%2==0:
        print(i,end=" ")