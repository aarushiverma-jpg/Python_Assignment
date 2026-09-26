for i in range(1,7):
    for j in range(1,5):
        if(j==1 and (i==2 or i==5)) or ((i==1 or i==3 or i==6) and j==2) or (j==3 and (i==1 or i==4 or i==6)) or (j==4 and (i==2 or i==5)):
            print("* ",end=" ")
        else:
            print(" ",end=" ")
    print()
