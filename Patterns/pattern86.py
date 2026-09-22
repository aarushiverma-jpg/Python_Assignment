for i in range(1,6):
    for j in range(10,i-1,-1):
        if(j==6 and i>1) or (j==7 and i>2) or (j==8 and i>3) or (j==9 and i>4):
            print(" ",end="")
        else:
            print("*",end="")
    print()