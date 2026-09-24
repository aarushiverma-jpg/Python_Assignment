for i in range(1,5):
    for j in range(1,6):
        if((j==1 or j==5) and (i<4)) or ((j==2 or j==4) and (i==4)):
            print("*",end="")
        else:
            print(" ",end="")
    print()