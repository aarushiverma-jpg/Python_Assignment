s="ugfvoducyscvtyrfaajnlnvdwv"
vowel_count=consonent_count=0
vowels={'a','e','i','o','u','A','E','O','I','U'}
for ch in s:
    if ch in vowels:
        vowel_count+=1
    elif 65<=ord(ch)<=90 or 97<=ord(ch)<=122:
        consonent_count+=1

print(F"vowels are {vowel_count} and consonents are {consonent_count}")