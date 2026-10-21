print("1. Crisps - 100p")
print("2. Chocolate - 150p")
print("3. Water - 120p")
print("4. Quit")
user_choice = int(input("Please select an option: "))

if user_choice == 1:
    print("You selected Crisps. Price: 100p")
elif user_choice == 2:
    print("You selected Chocolate. Price: 150p")
elif user_choice == 3:
    print("You selected Water. Price: 120p")
elif user_choice == 4:
    print("Thank you for using the vending machine")
else:
    print("Invalid selection. Please try again")