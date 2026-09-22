for i in range(10,0,-2):
    for k in range(10,i+1,-2):
        print(" ",end="")
    for j in range(1,i):
        if j%2==0:
            print(" ",end="")
        else:
            print(i//2,end="")
    print()