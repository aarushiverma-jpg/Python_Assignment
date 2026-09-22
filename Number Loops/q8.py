n = int(input("Enter a number:"))
i=0
first=0
second=1
tempory=0

while(i!=n):
    print(first,end=" ")
    tempory=first+second
    first=second
    second=tempory
    i+=1
    