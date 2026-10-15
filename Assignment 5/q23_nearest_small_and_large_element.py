n=int(input("Enter the size of array:"))
print("Enter the array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

target=int(input("Enter a num:"))

min=None
max=None

for element in a:
    if element<target:
        if min==None or min<element:
            min=element
    if element>target:
        if max==None or max>element:
            max=element

if max is not None:
    print(f"Nearest largest number close to {target} is {max}")
else:
    print(f"No nearest largest number close to {target} exist..")
if min is not None:
    print(f"Nearest smallest number close to {target} is {min}")
else:
    print(f"No nearest smallest number close to {target} exist..")