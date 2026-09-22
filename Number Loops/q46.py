import math
n=int(input("Enter a number:"))
if n<10:
    print(n)
else:
    last_digit=n%10
    length=int(math.log10(n))
    first_digit=n//(10**length)
    sum=first_digit+last_digit
    print(f" summation is {sum}")