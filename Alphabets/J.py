for i in range(1,6):
    for j in range(1,6):
        if(i==1) or (j==5):
            print("* ",end="")
        elif (i==5 and j==2) or (i==4 and j==1):
            print("*",end="")
        else:
            print(" ",end="")
    print()