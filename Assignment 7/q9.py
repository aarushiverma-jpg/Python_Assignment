d={
    'a':10,
    'b':60,
    'c':30,
    'd':20,
    'e':50,
    'f':55
}

max=0
max_key=""

for key,value in d.items():
    if max<value:
        max=value
        max_key=key

print(f"Maximum value in dictionary is {max} and the key is {max_key}")