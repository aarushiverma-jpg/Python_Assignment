n=int(input("Enter a number:"))
sum=0
reverse=0
count=0
while n:
    sum=sum*10+n%2
    n=n//2
    count+=1
while count:
    reverse=reverse*10+sum%10
    sum=sum//10
    count-=1
print(reverse)