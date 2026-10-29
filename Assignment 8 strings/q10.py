s="Oracle  java Foundation    "
lis=list(s)

for i in range(len(lis)):
    if ord(lis[i])==ord(" "):
        lis[i]="-"

hyphen="".join(lis)
print(f"'{s}' with hyphen is '{hyphen}'")