for i in range(5,0,-1):
    for j in range(1,i+1):
        if (i==4 and (j==2 or j==3)) or (j==2 and (i==4 or i==3)):
            print(" ",end="")
        else:
            print(i,end="")
    print()