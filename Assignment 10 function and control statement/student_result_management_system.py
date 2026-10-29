def calculate_total(marks_list):
    return sum(marks_list)

def calculate_percentage(total_marks, num_subjects):
    return total_marks / num_subjects

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 40:
        return "Pass"
    else:
        return "Fail"

def check_pass_fail(percentage):
    if percentage >= 40:
        return "Passed"
    else:
        return "Failed"

student_records = {}      
class_percentages = []    
num_subjects = 5

while True:
    name = input("Enter the student's name: ")
    
    marks = [] 
    
    print(f"--- Enter marks for {name} ---")
    
    for i in range(1, num_subjects + 1):
        mark = int(input(f"Subject {i} (0-100): "))
                
        if 0 <= mark <= 100:
            marks.append(mark)
        else:
            print("Invalid input! Marks must be between 0 and 100.")
                
    total = calculate_total(marks)
    percentage = calculate_percentage(total, num_subjects)
    grade = calculate_grade(percentage)
    status = check_pass_fail(percentage)
    
    student_records[name] = {
        'Marks': marks,
        'Total': total,
        'Percentage': percentage,
        'Grade': grade,
        'Status': status
    }
    
    class_percentages.append(percentage)
    
    choice = input("\nDo you want to enter details for another student? (y/n): ").lower()
    if choice == 'n':
        print("\nThank you for you time... \nHave a nice day...")
        break

print("--- FINAL RESULT SHEET ---")
print("="*40)

for student, data in student_records.items():
    print(f"Name: {student}")
    print(f"Marks: {data['Marks']}")
    print(f"Total: {data['Total']}/500")
    print(f"Percentage: {data['Percentage']}%")
    print(f"Grade: {data['Grade']} ({data['Status']})")
    print("-" * 40)

if len(class_percentages) > 0:
    class_average = sum(class_percentages) / len(class_percentages)
    print(f"Total Students: {len(student_records)}")
    print(f"Class Average Percentage: {round(class_average, 2)}%")