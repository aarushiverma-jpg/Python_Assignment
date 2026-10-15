x=[[1,2,3,4],[5,6,7,8],[2,6,7,8]]
max=0
max_row=0
min=100
min_row=0

for r in range(len(x)):
    sum=0
    for element in (x[r]):
        sum=sum+element
    if max<sum:
        max=sum
        max_row=r
    if min>sum:
        min=sum
        min_row=r

x[min_row],x[max_row]=x[max_row],x[min_row]
print(x)