n=int(input("Enter 1st year:"))
m=int(input("Enter 2nd year:"))
print(f"Leap year between {n} and {m} are:",end=" ")
for i in range(n+1,m):
    if i%400==0:
        print(i,end=" ")
        continue
    elif i%100==0:
        continue
    elif i%4==0:
        print(i,end=" ")
        continue
    else:
        continue