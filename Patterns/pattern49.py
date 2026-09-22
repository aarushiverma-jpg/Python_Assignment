for i in range(5,0,-1):
    for k in range(i,1,-1):
        print(" ",end="")
    m=1
    for j in range(1,7-i):
        print(m,end="")
        if m==1:
            m=0
        else:
            m=1
    print()