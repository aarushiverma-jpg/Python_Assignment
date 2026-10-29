def revese_the_sentence(sentence):
    lis=sentence.split()

    left=0
    right=len(lis)-1

    while left<right:
        lis[left],lis[right]=lis[right],lis[left]
        left+=1
        right-=1

    return " ".join(lis)

sentence="Python is easy"
reverse=revese_the_sentence(sentence)
print(reverse)