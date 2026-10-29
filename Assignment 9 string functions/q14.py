def remove_digits(s):
    lis=list(s)

    for i in range(len(lis)-1,-1,-1):
        if 48<=ord(lis[i])<=57:
            lis.pop(i)

    s="".join(lis)
    return s
s="e45rutgyvff56t7yiu"
without_digit=remove_digits(s)
print(f"{s} without digits is {without_digit}") 