n=int(input("Enter the size of 1st array:"))
print("Enter the 1st array:")
a=[]
for _ in range(n):
    i =int(input())
    a.append(i)

m=int(input("Enter the size of 2nd array:"))
print("Enter the 2nd array:")
b=[]
for _ in range(m):
    i =int(input())
    b.append(i)

i=0
j=0
union=[]
intersection =[]

while i<n and j<m:
    if a[i]==b[j]:
        if not union or union[-1]!=a[i]:
            union.append(a[i])
        if not intersection or intersection[-1]!=a[i]:
            intersection.append(a[i])
        i+=1
        j+=1
    elif a[i]<b[j]:
        if not union or union[-1]!=a[i]:
            union.append(a[i])
        i+=1
    else:
        if not union or union[-1]!=b[j]:
            union.append(b[j])
        j+=1

while i<n:
    if not union or union[-1]!=a[i]:
        union.append(a[i])
    i+=1

while j<m:
    if not union or union[-1]!=b[j]:
        union.append(b[j])
    j+=1

print(f"The union is {union} and length is {len(union)}")
print(f"The intersection is {intersection} and length is {len(intersection)}")


# while i<n and j<m:
#     if a[i]<b[j]:
#         if len(union)==0 or union[-1]!=a[i]:
#             union.append(a[i])
#         i+=1
#     else:
#         if len(union)==0 or union[-1]!=b[j]:
#             union.append(b[j])
#         j+=1
# while i<n:
#     if len(union)==0 or union[-1]!=a[i]:
#         union.append(a[i])
#     i+=1
# while j<m:
#     if len(union)==0 or union[-1]!=b[j]:
#         union.append(b[j])
#     j+=1

# for i in range(n):
#     for j in range(m):
#         if a[i]==b[j]:
#             intersection.append(a[i])