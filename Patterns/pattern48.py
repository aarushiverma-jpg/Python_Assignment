for i in range(5,0,-1):
    for k in range(i,1,-1):
        print(" ",end="")
    for j in range(1,7-i):
        if (i==2 and (j==3 or j==2)) or (i==3 and j==2):
            print("_",end="")
        else:
            print(chr(j+64),end="")
    print()