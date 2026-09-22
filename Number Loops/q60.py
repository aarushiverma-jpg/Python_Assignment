n=int(input("Enter a number:"))
print(f"Square of all the numbers till {n}:",end=" ")
for i in range(1,n+1):
    print(i*i,end=" ")
print(f"\nCube of all the numbers till {n}:",end=" ")
for i in range(1,n+1):
    print(i*i*i,end=" ")
print(f"\nSquare root of all the numbers till {n}:",end=" ")
for i in range(1,n+1):
    print(f"{i**(1/2):.2f}",end=" ")