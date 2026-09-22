import math
n=int(input("Enter a number:"))
if n<10:
    print(n)
else:
  last_digit=n%10
  length=int(math.log10(n))
  first_digit=n//(10**length)
  middle=n%(10**length)
  middle=middle//10
  swapped=(last_digit*(10**length))+middle*10+first_digit
  print(swapped)