salary=int(input("Enter the salary: "))
experiance_year=int(input("Enter the years of experiance: "))

if(experiance_year>5):
    bonus=salary*0.05
else:
    bonus=0
print(f"Net bonus amount is {bonus} and total salary is {salary+bonus}")