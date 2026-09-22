for i in range(1,8):
    if i<=4:
        for k in range(4-i,0,-1):
            print(" ",end="")
        for j in range(1,2*i):
            print("*",end="")
    else:
        for k in range(0,i-4):
            print(" ",end="")
        for j in range(8-(2*(i-4)),1,-1):
            print("*",end="")
    print()