def remove_spaces(s):
    s=s.strip()
    lis=s.split()
    s="".join(lis)
    return s

s="  ij iyv uilguyy  hiytv b vb  "
s1=remove_spaces(s)
print(F"The string {s} without spaces is {s1}")