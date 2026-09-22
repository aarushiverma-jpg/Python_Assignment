for i in range(1,8):
    if i<4:
        for k in range(1,i+1):
            print("x",end="")
    else:
        for j in range(i-4,4):
            print("x",end="")
    print()