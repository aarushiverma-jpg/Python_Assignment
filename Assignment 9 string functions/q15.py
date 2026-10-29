def print_ch(s):
    if len(s)==0:
        return
    else:
        print(f"{s[0]}-->{ord(s[0])}")
        print_ch(s[1:])
    
s="cfgvhhfhs"
print_ch(s)