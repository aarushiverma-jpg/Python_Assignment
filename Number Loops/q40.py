n=int(input("Enter a number:"))
even_count=0
odd_count=0

while(n!=0):
    r=n%10
    if(r%2==0):
        even_count+=1
    else:
        odd_count+=1
    n=n//10
print(f"even count is {even_count} and odd count is {odd_count}")
