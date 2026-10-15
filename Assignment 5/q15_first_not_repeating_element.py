n=int(input("Enter the size of array:"))
print("Enter the array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

print("First not repeating element is: ")
s=set()
result=None

for i in range(n-1,-1,-1):
    if a[i] not in s:
        result=a[i]
    s.add(a[i])
if result is not None:
    print(result) 
else:
    print("All are repeating numbers")   