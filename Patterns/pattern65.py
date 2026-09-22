k=1
for i in range (1,6):
    for _ in range(5,i,-1):
        print(" ",end="")
    for j in range(1):
        print(k,end="")
        k=k*11
    print()