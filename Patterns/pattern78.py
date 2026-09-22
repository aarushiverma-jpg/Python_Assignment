for i in range(1,8):
    if i<4:
        for k in range(1,5-i):
            print(" ",end="")
        for j in range(1,i+1):
            print(j,end="")
    else:
        for k in range (8-i,4):
            print(" ",end="")
        for j in range(1,5-(i-4)):
            print(j,end="")
    print()