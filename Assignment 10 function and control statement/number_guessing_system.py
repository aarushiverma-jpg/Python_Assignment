import random
while True:
    number=random.randint(1,100)
    level=input("Enter level of difficulty (e/m/h):")
    if level=='m':
        for i in range(7):
            guess_num=int(input("Guess the number:"))
            if guess_num>number:
                print("\nToo high\n")
                print(f"Attempts left {6-i}")
            elif guess_num<number:
                print("\nToo low\n")
                print(f"Attempts left {6-i}")
            else:
                print("\nYou have guessed the number!!\n")
                break
        else:
            print(f"\nYou have cross the attempt limits.. The number was {number}\n")
    if level=='e':
        for i in range(12):
            guess_num=int(input("Guess the number:"))
            if guess_num>number:
                print("\nToo high\n")
                print(f"Attempts left {11-i}")
            elif guess_num<number:
                print("\nToo low\n")
                print(f"Attempts left {11-i}")
            else:
                print("\nYou have guessed the number!!\n")
                break
        else:
            print(f"\nYou have cross the attempt limits.. The number was {number}\n")
    if level=='h':
        for i in range(3):
            guess_num=int(input("Guess the number:"))
            if guess_num>number:
                print("\nToo high\n")
                print(f"Attempts left {2-i}")
            elif guess_num<number:
                print("\nToo low\n")
                print(f"Attempts left {2-i}")
            else:
                print("\nYou have guessed the number!!\n")
                break
        else:
            print(f"\nYou have cross the attempt limits.. The number was {number}\n")
    
    choice=input("Want to try again?(y/n)")
    if choice=='n' or choice=='N':
        print("\nThank you for you time... \nHave a nice day...")
        break
