d={
    'a':10,
    'b':60,
    'c':30,
    'd':20,
    'e':50,
    'f':55,
    'g':23,
    'h':35,
    'i':40
}

threshold=30

result={}

for key,value in d.items():
    if value>=threshold:
        result[key]=value

print("Old Dictionary is :")
print(d)
print(f"The threshold is {threshold}")
print("New dictionary is :")
print(result)