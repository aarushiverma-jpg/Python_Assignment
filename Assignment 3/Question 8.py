class_held=int(input("Enter the number of classes held:"))
class_attened=int(input("Enter the number of classes attended:"))

percentage=(class_attened/class_held)*100

medical=input("is the student has medical cause (Y/N): ")
if(percentage>=75):
    print(f"Percentage is {percentage} and the student is allowd to sit in the exam")
elif (medical=='Y'):
    print(f"Percentage is {percentage} and the student is allowd to sit in the exam due to medical cause")
else:
    print(f"Percentage is {percentage} and the student is not allowd to sit in the exam")