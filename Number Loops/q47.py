n=int(input("Enter 1st number:"))
m=int(input("Enter 2nd number:"))
for i in range (n+1,m):
    print(f"table of {i}:",end=" ")
    for j in range(1,11):
        print(i*j,end=" ")
    print()