for i in range(1,8):
    if i<4:
        for j in range(1,i+1):
            if j==1 or j==i:
                print(j,end="")
            else:
                print(" ",end="")
    else:
        for j in range(1,9-i):
            if j==1 or j==8-i:
                print(j,end="")
            else:
                print(" ",end="")
    print()