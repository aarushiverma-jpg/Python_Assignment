for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        if(i==4 and (j==2 or j==3)) or (i==3 and j==2):
            print("_",end="")
        else:
            print("X",end="")
    print()