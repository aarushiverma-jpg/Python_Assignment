def remove_target(word,target):
    lis=list(word)

    for i in range(len(lis)-1,-1,-1):
        if lis[i] == target:
            lis.remove(lis[i])

    return "".join(lis)

word="qwertyuioyp"
target='y'
word_without_target=remove_target(word,target)
print(f"Word before {word} and word after {word_without_target}")