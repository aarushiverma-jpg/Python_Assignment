for i in range(1,7):
    for j in range(1,6):
        if(j==1 and 5>i>1) or (j==3 and i==4):
            print("*",end="")
        elif  (j==4 and (1<i<5))or (i==6 and j==5):
            print(" *",end="")
        elif ((j==2 or j==3) and (i==1 or i==5)) :
            print("* ",end="")
        else:
            print(" ",end="")
    print()
