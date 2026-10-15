x=[[1,2,3,4],[5,6,7,8],[2,6,7,8]]
for row in range(len(x)):
    l=0
    r=len(x[row])-1
    for c in range(len(x[row])//2):
        x[row][r],x[row][l]=x[row][l],x[row][r]
        l=l+1
        r=r-1
print(x)