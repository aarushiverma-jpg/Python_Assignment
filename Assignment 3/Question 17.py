salary=int(input("Enter the salary:"))
if(salary<=10000):
    hra_rate=0.20
    da_rate=0.80
elif(salary<=20000):
    hra_rate=0.25
    da_rate=0.90
elif(salary>20000):
    hra_rate=0.30
    da_rate=0.95

hra=salary*hra_rate
da=salary*da_rate
gross_salary=salary+hra+da
print(F"Gross salary is {gross_salary}")