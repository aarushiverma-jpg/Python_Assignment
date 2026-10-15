n=int(input("Enter the size of array:"))
print("Enter an array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

print("Negative at the last in an array is:")

pos=[i for i in a if i>=0]
neg=[i for i in a if i<0]
a=pos+neg

print(a)