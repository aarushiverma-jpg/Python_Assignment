grade=int(input("Enter your grade:"))
if(grade<60):
    print("Your grade is 'D'")
elif(grade>=60 and grade<=80):
    print("Your grade is 'C'")
elif(grade>80 and grade<=90):
    print("Your grade is 'B'")
elif(grade>90 and grade<=100):
    print("Your grade is 'A'")