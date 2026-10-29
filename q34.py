s="aaaabbbbccccddee"
d={}

for ch in s:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1

sub=""
for ch,val in d.items():
    sub+=ch+str(val)

print(f"Compressed String is {sub}")