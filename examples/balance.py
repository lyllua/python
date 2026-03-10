balance = 1000
option = 0

while option != 4:
    print("\n1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Exit")

    option = int(input("Choose an option: "))

    if option == 1:
        money = float(input("Amount to deposit: "))
        balance += money

    elif option == 2:
        money = float(input("Amount to withdraw: "))
        if money <= balance:
            balance -= money
        else:
            print("Not enough money!")

    elif option == 3:
        print("Balance:", balance)

    elif option == 4:
        print("Exiting...")

    else:
        print("Invalid option! Please choose 1-4.")