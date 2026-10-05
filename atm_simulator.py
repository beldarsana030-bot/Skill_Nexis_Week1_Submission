# Skill Nexus - Week 1 Mini Project
# Simple ATM Simulator

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
STARTING_BALANCE = 1000.00


def login():
    """Authenticate the user using a PIN."""
    for attempt in range(1, MAX_ATTEMPTS + 1):
        pin = input("Enter your 4-digit PIN: ")

        if pin == CORRECT_PIN:
            print("\nLogin successful!")
            return True

        remaining = MAX_ATTEMPTS - attempt
        if remaining > 0:
            print(f"Incorrect PIN. {remaining} attempt(s) remaining.")
        else:
            print("Too many incorrect attempts.")

    return False


def check_balance(balance):
    """Display the current account balance."""
    print(f"\nCurrent balance: Rs. {balance:.2f}")
    return balance


def deposit(balance):
    """Deposit money into the account."""
    try:
        amount = float(input("Enter deposit amount: Rs. "))

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return balance

        balance += amount
        print(f"Deposit successful. New balance: Rs. {balance:.2f}")
    except ValueError:
        print("Please enter a valid amount.")

    return balance


def withdraw(balance):
    """Withdraw money if sufficient funds are available."""
    try:
        amount = float(input("Enter withdrawal amount: Rs. "))

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return balance

        if amount > balance:
            print("Insufficient balance.")
            return balance

        balance -= amount
        print(f"Withdrawal successful. New balance: Rs. {balance:.2f}")
    except ValueError:
        print("Please enter a valid amount.")

    return balance


def atm_menu():
    """Run the ATM menu after successful login."""
    balance = STARTING_BALANCE

    while True:
        print("\n===== SIMPLE ATM SIMULATOR =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


def main():
    print("===== WELCOME TO SIMPLE ATM =====")

    if login():
        atm_menu()
    else:
        print("Access denied.")


if __name__ == "__main__":
    main()
