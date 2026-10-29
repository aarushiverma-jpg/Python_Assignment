def count_words(s):
    s=s.strip()
    lis=s.split()
    no_of_words=len(lis)
    return no_of_words

s=" Info beans Foundation   "
no_of_words=count_words(s)
print(f"The number of words are {no_of_words}")