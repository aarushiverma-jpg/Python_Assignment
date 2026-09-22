for i in range(1,8):
    for j in range(1,8):
        if j==4 and i==4:
            print("X",end="")
        elif(i==j):
            print("\\",end="")
        elif(i+j==8):
            print("/",end="")
        elif i==1 or i==7:
            print("_",end="")
        elif j==1 or j==7:
            print("|",end="")
        else:
            print(" ",end="")
    print()