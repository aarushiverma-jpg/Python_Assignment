n=int(input("Enter 1st number:"))
m=int(input("Enter 2nd number:"))
for i in range (n+1,m):
    print(f"factors of {i}:",end=" ")
    for j in range(1,i+1):
        if i%j==0:
            print(j,end=" ")
    print()