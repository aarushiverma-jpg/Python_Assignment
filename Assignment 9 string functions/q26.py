def longest_word(s):
    lis=s.split()
    d={}

    for word in lis:
        d[word]=len(word)

    max=0
    for key,value in d.items():
        if max<value:
            max=value
            max_key=key
    return max_key

sentence="Python is easy"
word=longest_word(sentence)
print(f"Longest word is {word}")