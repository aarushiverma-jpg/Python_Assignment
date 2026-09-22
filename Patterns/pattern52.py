for i in range(5,0,-1):
    for k in range(i,5):
        print(" ",end="")
    for j in range(1,i+1):
        if (i==4 and (j==2 or j==3)) or (i==3 and j==2):
            print("_",end="")
        else:
            print(j,end="")
    print()