d={
    'a':10,
    'b':60,
    'c':30,
    'd':20,
    'e':50,
    'f':55
}

max=max2=0

for key,value in d.items():
    if value>max:
        max2=max
        max=value
    elif max2<value<max:
        max2=value

print(f"second maximum value is {max2} and maximum value is {max}")