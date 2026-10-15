d1={
    'a':10,
    'b':60,
    'c':30,
    'd':55
}

d2={
    'a':10,
    'e':60,
    'c':55,
    'd':55
}

result={}

for key,value in d1.items():
    if (key in d2) and (d2[key]==value):
        result[key]=value

print("Comman keys in both dictionaries are :")
print(result)