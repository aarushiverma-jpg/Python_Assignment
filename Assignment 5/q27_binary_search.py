n=int(input("Enter the size of array:"))
print("Enter a sorted array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

k=int(input("Enter number you want to search"))
low=0
high=n-1
flag=False

while low<high:
    mid=(low+high)//2
    if a[mid]==k:
        print(f"Element found at {mid} index")
        flag=True
        break
    elif a[mid]>k:
        high=mid-1
    else:
        low=mid+1
if not flag:
    print("Element not found")