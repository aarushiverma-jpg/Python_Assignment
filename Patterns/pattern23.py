k=1
for i in range(1,6):
    for j in range(1,i+1):
        if j==1 or j==i or i==5:
            print(chr(k+96),end="")
        else:
            print(" ",end="")
        k+=1
    print()