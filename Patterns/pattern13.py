for i in range(1,6):
    for j in range(1,i+1):
        print(chr(j+96),end="")
    print()
k=1
for i in range(1,6):
    for j in range(1,i+1):
        print(k,end="")
        if k==1:
            k=0
        else:
            k=1
    print()