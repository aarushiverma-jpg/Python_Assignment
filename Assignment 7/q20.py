d={
    'a':10,
    'b':60,
    'c':30,
    'd':20,
    'e':50,
    'f':55
}
print("Before reversing:")
print(d)

d={value:key for key,value in d.items()}

print("After reversing:")
print(d)