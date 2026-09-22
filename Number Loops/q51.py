n=int(input("Enter 1st number:"))
m=int(input("Enter 2nd number:"))
print("Reverse numbers are:",end=" ")
for i in range (n+1,m):
    sum=0
    while(i):
        sum=sum*10+i%10
        i//=10
    print(f"{sum}",end=" ")