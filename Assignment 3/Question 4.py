grade=int(input("Enter your grade:"))
if(grade<25 and grade>=0):
    print("Your grade is 'F'")
elif(grade>=25 and grade<45):
    print("Your grade is 'E'")
elif(grade>=45 and grade<50):
    print("Your grade is 'D'")
elif(grade>=50 and grade<60):
    print("Your grade is 'C'")
elif(grade>=60 and grade<80):
    print("Your grade is 'B'")
elif(grade>=80 and grade<=100):
    print("Your grade is 'A'")