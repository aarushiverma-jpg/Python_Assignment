s="GF$uiy%^RT&Yhu$%78876754tGYHBVDRgyhui"
digit=lower=upper=special=0
for ch in s:
    a_n=ord(ch)
    if 65<=a_n<=90:
        upper+=1
    elif 48<=a_n<=57:
        digit+=1
    elif 97<=a_n<=122:
        lower+=1
    elif 32<=a_n<=126:
        special+=1
    else:
        print("invalid symbol..")
        break
else:
    print(f"Lower case are {lower}")
    print(f"Upper case are {upper}")
    print(f"digits are {digit}")
    print(f"special symbols are {special}")