for i in range(10,0,-2):
    for k in range(10,i+1,-2):
        print(" ",end="")
    k=1
    for j in range(1,i):
        if j%2==0:
            print(" ",end="")
        else:
            print(chr(k+64),end="")
            k=k+1
    print()