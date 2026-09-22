first=int(input("Enter 1st number:"))
second =int (input("Enter 2nd number:"))

operator=input("What do you want to perform (+/>/==):")

if(operator=="+"):
    print(f"Addition of {first} and {second} is : {first+second}")
elif(operator==">"):
    print(f"{first} is greater than {second}") if first>second else print(f"{second} is greater than {first}")
elif(operator=="=="):
    print("Both the numbers are equal") if first==second else print("Both are not same")
else:
    print("Invaild operator")