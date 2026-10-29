def space_to_hyphen(s):
    lis=list(s)

    for i in range(len(lis)):
        if ord(lis[i])==ord(" "):
            lis[i]="-"

    s="".join(lis)
    return s

s="Oracle  java Foundation    "
hyphen=space_to_hyphen(s)
print(f"'{s}' with hyphen is '{hyphen}'")