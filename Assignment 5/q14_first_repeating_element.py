n=int(input("Enter the size of array:"))
print("Enter the array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

print("First repeating element is: ")
# list=[]
# for element in a:
#     if element not in a:
#         list.append(element)
#     else:
#         print(element)
#         break
flag=None
for i in range (n-1):
    for j in range(i+1,n):
        if a[i]==a[j]:
            flag=a[i]
            break
    if flag is not None:
        print(flag)
        break
else:
    print("Dosen't contain repeating element")  