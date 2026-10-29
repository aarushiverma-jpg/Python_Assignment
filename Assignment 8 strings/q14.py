s="e45rutgyvff56t7yiu"
lis=list(s)

for i in range(len(lis)-1,-1,-1):
    if 48<=ord(lis[i])<=57:
        lis.pop(i)

without_digit="".join(lis)
print(f"{s} without digits is {without_digit}") 