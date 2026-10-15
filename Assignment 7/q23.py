d={
    'a':10,
    'b':60,
    'c':30,
    'd':55
}

temp=d.copy()
result={}

print("The dictionary is:")
print(d)
print("Sorted dictionary by its values in ascending order.")

while temp:
    min=list(temp.keys())[0]
    for k in temp:
        if temp[k]<temp[min]:
            min=k
    result[min]=temp[min]
    del temp[min]

print(result)