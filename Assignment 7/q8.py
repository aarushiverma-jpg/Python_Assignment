d={
    'a':10,
    'b':'B',
    'c':30,
    'd':'D'
}

sum=0

for value in d.values():
    if isinstance(value,int):
        sum=sum+value
print(f"Sumation of the numeric values are {sum}")