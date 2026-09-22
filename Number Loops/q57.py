n=int(input("Enter 1st number:"))
m=int(input("Enter 2nd number:"))
print("Prime numbers are: ",end="")
for j in range (n+1,m):
    i=2
    while i<=j//2:
        if j%i==0:
            break
        i=i+1
    if i>j//2 and j>1:
        print(j,end=" ")