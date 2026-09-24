for i in range(1,6):
    for j in range(1,6):
        if(j==1) or (j==2 and i==3) or (j==3 and (i%2==0)) or (j==4 and (i==1 or i==5)):
            print("* ",end="")
        else:
            print(" ",end="")
    print()