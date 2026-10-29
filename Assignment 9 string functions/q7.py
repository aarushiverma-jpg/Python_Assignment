def lower_to_upper(s):
    lis=list(s)
    for i in range(len(lis)):
        if 97<=ord(lis[i])<=122:
            lis[i]=chr(ord(lis[i])-32)

    s="".join(lis)
    return s

s="DXCFghbjDFcgvh"
upper=lower_to_upper(s)
print(f"Upper case of {s} is {upper}")