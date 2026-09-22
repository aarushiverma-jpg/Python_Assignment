n=int(input("Enter a number:"))
if n>=2:
    a=1
    b=2
    print(f"{a} {b} ",end="")
    for _ in range(n-2):
        c=a*b
        print(c,end=" ")
        a=b
        b=c