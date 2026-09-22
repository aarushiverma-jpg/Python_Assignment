for i in range(10,0,-2):
    for k in range(10,i+1,-2):
        print(" ",end="")
    for j in range(1,i):
        if j==1 or j==i-1 or i==10:
            print(j,end="")
        else:
            print(" ",end="")
    print()