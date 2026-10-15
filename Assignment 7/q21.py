d1={
    'a':10,
    'b':60,
    'c':30,
}

d2={
    'a':20,
    'b':50,
    'd':55
}

print("Before merging:")
print(d1)
print(d2)
print("After merging:")

for key,value in d2.items():
    d1[key]=d1.get(key,0)+value

print(d1)