def count(s):
    vowel_count=consonent_count=0
    vowels={'a','e','i','o','u','A','E','O','I','U'}
    for ch in s:
        if ch in vowels:
            vowel_count+=1
        elif 65<=ord(ch)<=90 or 97<=ord(ch)<=122:
            consonent_count+=1
    return vowel_count,consonent_count

s="abcdefghijklmnopqrstuvwxyz"

v_c,c_c=count(s)
print(F"vowels are {v_c} and consonents are {c_c}")