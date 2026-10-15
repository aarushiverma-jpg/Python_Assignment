x=[[1,2,3],[4,5,6],[7,8,9]]
for r in range(len(x)):
    for c in range(len(x[r])):
        if r==c or r+c==2:
            print(x[r][c],end=" ")