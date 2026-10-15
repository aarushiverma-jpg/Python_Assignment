d1={
    'a':10,
    'b':60,
    'c':30,
    'd':55
}

d2={
    'a':20,
    'b':50,
    'd':55
}

key1=list(d1.keys())
key2=list(d2.keys())

key=set(key1+key2)
result=[]

for k in key:
    if k in d1 and k in d2:
        result.append(k)

print(result)