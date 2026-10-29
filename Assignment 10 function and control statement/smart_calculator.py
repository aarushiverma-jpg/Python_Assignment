def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def divide(a,b):
    return a/b

def mod(a,b):
    return a%b

def fl_divide(a,b):
    return a//b

def power(a,b):
    return a**b

def enter_num():
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    print()
    return a,b

while True:
    print("For addition type '+'")
    print("For subtraction type '-'")
    print("For multiplication type '*'")
    print("For division type '/'")
    print("For modulas type '%'")
    print("For floor division type '//'")
    print("For generating power type '**")
    print()
    choice=input("Enter your choice:")

    if choice=="+":
        a,b=enter_num()
        result=add(a,b)
        print(f"Addition of {a} and {b} is {result}")

    elif choice=="-":
        a,b=enter_num()
        result=sub(a,b)
        print(f"Subtraction of {a} by {b} is {result}")

    elif choice=="*":
        a,b=enter_num()
        result=multi(a,b)
        print(f"Multiplication of {a} and {b} is {result}")

    elif choice=="/":
        a,b=enter_num()
        if b!=0:
            result=divide(a,b)
            print(f"Division of {a} and {b} is {result}")
        else:
            print("Invalid Demominator...")

    elif choice=="%":
        a,b=enter_num()
        if b!=0:
            result=mod(a,b)
            print(f"Modulo of {a} and {b} is {result}")     
        else:
            print("Invalid Demominator...")

    elif choice=="//":
        a,b=enter_num()
        if b!=0:
            result=fl_divide(a,b)
            print(f"Floor division of {a} and {b} is {result}")     
        else:
            print("Invalid Demominator...")

    elif choice=="**":
        a,b=enter_num()
        result=power(a,b)
        print(f"{a} raise to {b} is {result}")

    elif choice=="exit" or choice=="Exit" or choice=="EXIT":
        print("\nThank you for you time... \nHave a nice day...")
        break
    else:
        print("Invalid operation....choose one from the options....")

    print()
