print("1. Crisps - 100p")
print("2. Chocolate - 150p")
print("3. Water - 120p")
print("4. Quit")
balance = 200
print("Your balance is", balance, "p")
while balance > 0:
    user_choice = int(input("Please select an option: "))

    if user_choice == 1:
        print("You selected Crisps. Price: 100p")
        if balance > 100:
            balance = balance - 100
            print("Purchase successful")
            print("Remaining balance:", balance, "p")
        else:
            print("Insufficient funds. Please choose a cheaper product.")
    elif user_choice == 2:
        print("You selected Chocolate. Price: 150p")
        if balance > 150:
                balance = balance - 150
                print("Purchase successful")
                print("Remaining balance:", balance, "p")
        else:
            print("Insufficient funds. Please choose a cheaper product.")
    elif user_choice == 3:
        print("You selected Water. Price: 120p")
        if balance > 120:
                balance = balance - 120
                print("Purchase successful")
                print("Remaining balance:", balance, "p")
        else:
            print("Insufficient funds. Please choose a cheaper product.")
    elif user_choice == 4:
        print("Thank you for using the vending machine")
        break
    else:
        print("Invalid selection. Please try again")