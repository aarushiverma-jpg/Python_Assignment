for i in range(1,6):
    for k in range(6,7-i,-1):
        print(" ",end="")
    for j in range(5,i-1,-1):
        print(i,end="")
    print()