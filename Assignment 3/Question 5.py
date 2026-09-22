val1=int(input("Enter 1st value: "))
val2=int(input("Enter 2nd value: "))
val3=int(input("Enter 3rd value: "))

if(val1>=val2 and val1>=val3):
    max=val1
elif(val2>=val1 and val2>=val3):
    max=val2
else:
    max=val3

if(val1<=val2 and val1<=val3):
    min=val1
elif(val2<=val1 and val2<=val3):
    min=val2
else:
    min=val3

print(f"{max} is maximum and {min} is minimum.")