for i in range(1,6):
    for j in range(1,6):
        if(j==1) or (j==5) or (j%2==0 and i==2) or (j==3 and i==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
