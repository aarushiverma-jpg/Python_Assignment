x=[[1,2,13],[4,55,6],[7,8,9]]
max=0
index=[]

for row in x:
    sum=0
    for element in row:
        sum=sum+element
    if max<sum:
        max=sum
        index=row

print(f"maximum sum of a row is {max} and the row is {index}")