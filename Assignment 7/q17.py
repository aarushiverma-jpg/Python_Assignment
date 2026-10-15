list=[1, 2, 2, 3, 1, 2]
d={}

for l in list:
    if l in d:
        d[l]+=1
    else:
        d[l]=1
print("Frequency of each character in a list:")
print(d)