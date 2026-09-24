for i in range(1,6):
    for j in range(1,4):
        if (j==1 or (j==2 and (i==5 or i==1)) or (j==3 and (i!=1 and i!=5))):
            print("* ",end="")
        else:
            print(" ",end="")
    print()