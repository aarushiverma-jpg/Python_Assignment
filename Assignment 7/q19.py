list=[1, 2, 2, 3, 1, 2]
d={}

for l in list:
    if l in d:
        d[l]+=1
    else:
        d[l]=1

duplicates={}
print("Duplicate elements in a list and their frequencies are:")
for key,value in d.items():
    if value>1:
        duplicates[key]=value

print(duplicates)