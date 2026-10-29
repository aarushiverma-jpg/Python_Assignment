s="a4b3cd2e5"
word=""
result=""

for ch in s:
    if ch.isdigit():
        result+= word*int(ch)
        word=""
    else:
        word+=ch

print(f"Expanded string is {result}")