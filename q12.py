s1="aabaa"
s2="aaba"

if len(s1)!=len(s2):
    print("Not equal..")
else:
    for i in range(len(s1)):
        if ord(s1[i])-ord(s2[i]):
            print("Strings are not equal..")
            break
        else:
            print("Strings are equal..")