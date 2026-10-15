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

print("Merging A and B in C (differeciated by even and odd):")
even_a=[i for i in a if i%2==0]
odd_a=[i for i in a if i%2==1]

even_b=[i for i in b if i%2==0]
odd_b=[i for i in b if i%2==1]

c=even_a + even_b + odd_b[::-1] + odd_a[::-1]

print(c)