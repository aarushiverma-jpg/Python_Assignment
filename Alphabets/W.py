for i in range(1,5):
    for j in range(1,10):
        if(j<5 and (i==j)) or (j>5 and (i+j==10)) or (j==5 and i==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()