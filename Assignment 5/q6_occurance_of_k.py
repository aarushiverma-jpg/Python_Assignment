n=int(input("Enter the size of array:"))
print("Enter an array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

k=int(input("Enter an integer number:"))

count=0

for element in a:
    if element==k:
        count+=1

print(f"The occurance of {k} is {count}")