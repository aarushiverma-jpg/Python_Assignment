gender=input("Enter gender of employee (M/F):")
age=int(input("Enter the age:"))
marital=input("Enter the marital status (Y/N):")
if(gender=='M'):
    if(age<40 and age>=20):
        print("The employee can work anywhere.")
    elif(age>=40 and age<=60):
        print("The employee will work from urban areas only.")
    else:
        print("ERROR")
elif(gender=='F'):

    print("The employee will work from urbam areas only.")
else:
    print("ERROR")