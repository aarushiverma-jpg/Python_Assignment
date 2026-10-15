x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[7,8,9],[4,5,6],[1,2,3]]

z=[[0,0,0],[0,0,0],[0,0,0]]

for row in range(len(x)):
    for col in range(len(y[0])):
        for k in range(len(x[0])):
            z[row][col]=z[row][col]+(x[row][k]*y[k][col])

print(z)