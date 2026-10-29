def expand_string(s):
    word=""
    result=""

    for ch in s:
        if ch.isdigit():
            result+= word*int(ch)
            word=""
        else:
            word+=ch
    return result

s="a4b3cd2e5"
str=expand_string(s)
print(f"Expanded string is {str}")