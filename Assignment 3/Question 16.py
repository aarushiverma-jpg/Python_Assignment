physics=int(input("Enter the marks of physics:"))
chemistry=int(input("Enter the marks of chemistry:"))
biology=int(input("Enter the marks of biology:"))
mathematics=int(input("Enter the marks of mathematics:"))
computer=int(input("Enter the marks of computer:"))

grade=(physics+chemistry+biology+mathematics+computer)/5

if(grade>=90):
    print(f"Your percentage is {grade} grade is 'A'")
elif(grade>=80):
    print(f"Your percentage is {grade} grade is 'B'")
elif(grade>=70):
    print(f"Your percentage is {grade} grade is 'C'")
elif(grade>=60):
    print(f"Your percentage is {grade} grade is 'D'")
elif(grade>=40):
    print(f"Your percentage is {grade} grade is 'E'")
elif(grade<40):
    print(f"Your percentage is {grade} grade is 'F'")