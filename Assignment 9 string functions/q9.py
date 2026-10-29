def first_and_last(s):
    first=s[0]
    last=s[-1]
    return first,last

s="tyuuhljmhdxcfvg"
first,last=first_and_last(s)
print(f"First letter is {first}")
print(f"Last letter is {last}")