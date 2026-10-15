li=["eat", "tea", "bat", "ate", "tab","water", "terwa"]
result={}
for word in li:
    key="".join(sorted(word))
    if key in result:
        result[key].append(word)
    else:
        result[key]=[word]

print("Groups are:")
for value in result.values():
    print(value)