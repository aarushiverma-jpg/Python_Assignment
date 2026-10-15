n=int(input("Enter the size of array:"))
print("Enter the array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

count=0
cs=0
print("Subarray with equal 0s and 1s: ")
for i in range(n):
    cs=0
    for j in range(i,n):
        if a[j]==0:
             cs=cs-1
        else:
             cs=cs+1
        if cs==0:
            print(f"({i},{j})",end=" ")
            count+=1

print(f"\n{count}")