n=int(input("Enter a number:"))
temp=n
sum=0
while(n):
    sum=sum*10+(n%10)
    n=n//10
if(sum==temp):
    print("Palindrome")
else:
    print("Not Palindrome")