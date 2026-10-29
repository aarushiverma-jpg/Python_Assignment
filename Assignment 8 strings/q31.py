s="abcabcbb"

l=r=max=0
b=set()

for r in range(len(s)):
    ch=s[r]
    if ch in b:
        b.remove(s[l])
        l+=1
    b.add(s[r])
    if (r-l+1)>max:
        max=r-l+1
        i=l
        j=r

sub=s[i:j+1]
print(f"Max sub string with no repetation is {sub} and max length is {max}")