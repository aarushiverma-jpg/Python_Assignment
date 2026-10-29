def length_checker(password,suggestion,strength):
    if len(password)>=12:
        strength.append("Length of password")
    else:
        suggestion.append("Length is less than required length")

def number_check(password,suggestion,strength):
    if any(ch.isdigit() for ch in password):
        strength.append("Password contains numbers")
    else:
        suggestion.append("Password doesn't contain numbers")

def lower_check(password,suggestion,strength):
    if any(ch.islower() for ch in password):
        strength.append("Password contains lower characters")
    else:
        suggestion.append("Password doesn't contain lower characters")

def upper_check(password,suggestion,strength):
    if any(ch.isupper() for ch in password):
        strength.append("Password contains upper characters")
    else:
        suggestion.append("Password doesn't contain upper characters") 

def speacial_check(password,suggestion,strength):
    if any(ch in {'!','@','#','$','%','^','&','*','(',')','_','-','{','}','[',']',':',";","?",'/','\\',"|"} for ch in password):
        strength.append("Password contains special characters")
    else:
        suggestion.append("Password doesn't contain special characters") 

while True:
    suggestion=[]
    strength=[]

    password=input("Enter your password:")

    length_checker(password,suggestion,strength)
    number_check(password,suggestion,strength)
    lower_check(password,suggestion,strength)
    upper_check(password,suggestion,strength)
    speacial_check(password,suggestion,strength)

    print("Strengths are:")
    for s in strength:
        print(s)

    print("Suggestions are:")
    for s in suggestion:
        print(s)

    choice=input("Do you want to continue?(y/n): ")
    if choice=="n":
        print("\nThank you for you time... \nHave a nice day...")
        break    