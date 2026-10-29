word="qwertyuioyp"
target='y'
lis=list(word)

for i in range(len(lis)-1,-1,-1):
    if lis[i] == target:
        lis.remove(lis[i])

word_without_target="".join(lis)
print(f"Word before {word} and word after {word_without_target}")