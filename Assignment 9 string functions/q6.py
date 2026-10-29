def length(s):
    length=0
    for _ in s:
        length+=1
    return length

s="zsdcfgh"
length=length(s)
print(f"length of string is {length}")