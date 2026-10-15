n=int(input("Enter the size of array:"))
print("Enter an array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

k=int(input("Enter the element you want to search:"))

for element in a:
    if element==k:
        print(f"Element found...")
        break
else:
    print("Element not found...")