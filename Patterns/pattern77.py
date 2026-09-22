for i in range(1,8):
    if i<4:
        for j in range(1,i+1):
            print(j,end="")
    else:
        for j in range(1,5-(i-4)):
            print(j,end="")
    print()