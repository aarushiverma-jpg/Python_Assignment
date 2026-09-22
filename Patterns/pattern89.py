for i in range(0,12,2):
    for k in range((10-i)//2,0,-1):
        print(" ",end="")
    m=1
    for j in range(i+1):
        print(m,end="")
        if m==1:
            m=0
        else:
            m=1
    print()