n=int(input("enter the number of terms to print:"))
# even number
i=0
print(f"first {n} even number is:")
while n!=0:
    print(f"{i} ",end="")
    i+=2
    n-=1