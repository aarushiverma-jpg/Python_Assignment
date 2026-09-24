for i  in range(1,6):
    for _ in range(5,i,-1):
        print(" ",end="") 
    for j in range(1,2*i):
        if j==1 or j==2*i-1 or (j==3 and i==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()