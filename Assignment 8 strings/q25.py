word="1234a56789"

for ch in word:
    if 48<=ord(ch)<=57:
        continue
    else:
        print("String contains letters..")
        break
else:
    print("String contains only digits")