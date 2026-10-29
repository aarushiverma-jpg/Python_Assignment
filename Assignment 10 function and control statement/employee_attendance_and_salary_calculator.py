employee_details={}
no_of_employee=1
days_for_attendance=27
choice="y"
daily_wage=1000

def base_salary(days):
    global daily_wage
    return days*daily_wage

def attendance_percentage(days):
    global days_for_attendance
    return days/days_for_attendance*100

def bonus_or_deduction(percentage,base_salary):
    if percentage>=95:
        final_salary=base_salary*1.10
        status="Bonus of 10%"
    elif percentage>=75:
        final_salary=base_salary
        status="No bonus/No deduction"
    else:
        final_salary=base_salary*0.9
        status="Deduction of 10%"
    return final_salary, status

def generate_emp_details():
    print("Final Employee salary:\n")
    global employee_details
    for emp,info in employee_details.items():   
        print(f"Emp ID: {emp}")
        print(f"Emp Name: {info['name']}")
        print(f"Attendance: {info['attendance']}/{days_for_attendance} days ({info['percentage']}%)")
        print(f"Base Salary: ₹{info['base_salary']}")
        print(f"Rule Applied: {info['status']}")
        print(f"Final Salary: ₹{info['final_salary']}")
        print("-" * 30)

while True:
    if not employee_details or choice=='y':
        print("\nEnter details of employee:")
        employee_name=input("\nEnter the name of employee: ")
        employee_attendance=int(input(f"\nEnter the attendance of employee out of {days_for_attendance}: "))

        if not 0<=employee_attendance<=days_for_attendance:
            print("Employee days is invalid...try again..")
            continue

        percentage=attendance_percentage(employee_attendance)
        salary=base_salary(employee_attendance)
        final_salary,status=bonus_or_deduction(percentage,salary)

        emp_key=f'employe_{no_of_employee}'

        employee_details[emp_key]={
            'name':employee_name,
            'attendance':employee_attendance,
            'base_salary':salary,
            'percentage':percentage,
            'final_salary':final_salary,
            'status':status
        }

        no_of_employee+=1
        choice=input(f"\nDo you want to add details of employee {no_of_employee} (y/n): ")
        if choice=='n':
            print("\nGenerating reports...\n")
            break

generate_emp_details()
print("\nThank you for you time... \nHave a nice day...")