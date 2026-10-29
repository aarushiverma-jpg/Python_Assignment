saved_pin=12345
count=1
balance=10000

def check_balance():
    print(f"\nYour account balance is {balance}\n")

def deposit():
    adding_amount=int(input("Enter the amount you want to deposit in your account:"))
    global balance
    balance=balance+adding_amount
    print(f"\nYour balance after adding {adding_amount} is {balance}\n")

def withdrawal():
    withdrawal_amount=int(input("Enter the amount you want to withdraw from your account:"))
    global balance
    if balance>=withdrawal_amount:
        balance=balance-withdrawal_amount
        print(f"\nYour balance after withdrawal is {withdrawal_amount} is {balance}\n")
    else:
        print("\nYou dont have enough balance...\n")

while count<=3:
    pin=int(input("Enter your pin:"))
    if pin==saved_pin:
        while True:
            print("To check your balance type 1...")
            print("To deposit in your bank account type 2...")
            print("To withdraw from your account type 3...")
            print("To exit type e/E...")
            print()
            choice=input("Enter your choice:")

            if choice=='1':
                check_balance()
            elif choice=='2':
                deposit()
            elif choice=='3':
                withdrawal()
            elif choice=='e' or choice=='E':
                break
            else:
                print("\nInvalid input...\n")

        choice=input("Do you want to continue as a new user? (Y/N):")
        if choice=='N':
            print("\nThank you for you time... \nHave a nice day...")
            break
        else:
            count=1
            balance=10000
    else:
        print(f"\nInvalid Pin...You have {3-count} chances...\n")
        count+=1
