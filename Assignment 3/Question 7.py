class_held=int(input("Enter the number of classes held:"))
class_attened=int(input("Enter the number of classes attended:"))

percentage=(class_attened/class_held)*100

if(percentage>=75):
    print(f"Percentage is {percentage} and the student is allowd to sit in the exam")
else:
    print(f"Percentage is {percentage} and the student is not allowd to sit in the exam")