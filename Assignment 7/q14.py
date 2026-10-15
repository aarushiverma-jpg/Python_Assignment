d1={
    'a':10,
    'b':60,
    'c':30,
    'd':20,
    'e':50,
    'f':55
}

# d2=d1.copy()
d2=d1

print("Before changing:")
print(d1)
print(d2)

print("After changing:")
d1['a']=20

print(d1)
print(d2)