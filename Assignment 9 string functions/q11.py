def count_of(s,target):
    lis=list(s)
    count=0

    for i in range(len(lis)):
        if lis[i]==target:
            count+=1
    return count

s="Oracle  java Foundation    "
target="a"
count=count_of(s,target)
print(f"number of '{target}' occured in this string is {count}")