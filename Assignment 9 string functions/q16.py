def anagrams(s1,s2):
    d1={}
    for ch in s1:
        d1[ch]=d1.get(ch,0)+1

    d2={}
    for ch in s2:
        d2[ch]=d2.get(ch,0)+1

    if d1==d2:
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")

s1="listen"
s2="slient"
anagrams(s1,s2)