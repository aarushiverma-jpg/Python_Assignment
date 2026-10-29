s="Oracle  java Foundation    "
target=" "
lis=list(s)
count=0

for i in range(len(lis)):
    if lis[i]==target:
        count+=1

print(f"number of '{target}' occured in this string is {count}")