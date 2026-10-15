x=[[1,2,3,4],[5,6,7,8],[2,6,7,8]]

row=len(x)
col=len(x[0])

for j in range(col):
    temp=[]
    for i in range(row):
        temp.append(x[i][j])
    x.append(temp)

for _ in range(row):
    x.pop(0)

print(x)