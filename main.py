def show_balance(balance):
    print("*********************")
    print(f"Your balance is ${balance:.2f}")
    print("*********************")

def deposit():
    while True:
        print("*********************")
        try:
            amount = float(input("Enter an amount to be deposited: "))
            if amount < 0:
                print("That's not a valid amount.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def withdraw(balance):
    while True:
        print("*********************")
        try:
            amount = float(input("Enter amount to be withdrawn: "))
            if amount > balance:
                print("Insufficient funds.")
            elif amount < 0:
                print("Amount must be greater than 0.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
def main():
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print("   Banking Program   ")
        print("*********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("That is not a valid choice. Please choose between 1-4.")

    print("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()
