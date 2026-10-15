n=int(input("Enter the size of array:"))
print("Enter an array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

print("Peak element is at:",end=" ")
if n==1 or a[n-1]>a[n-2]:
    print("1")
else:
    for i in range(n-1):
        if i==0 and a[i]>a[i+1]:
            print('1')
            break
        if a[i]>=a[i-1] and a[i]>=a[i+1]:
           print('1') 
           break
    else:
        print("0")