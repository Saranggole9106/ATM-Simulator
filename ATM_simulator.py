class ATM:
    def __init__(self):
        # Initialize a dictionary to store account information
        self.accounts = {}  

    def create_account(self, account_number, pin):
        # Create a new account if it doesn't already exist
        if account_number in self.accounts:
            return False  # Account already exists
        self.accounts[account_number] = {"pin": pin, "balance": 0, "transactions": []}
        return True
    
    def authenticate(self, account_number, pin):
        # Check if the provided account number and PIN are valid
        account = self.accounts.get(account_number)
        if account and account["pin"] == pin:
            return True
        return False

    def deposit(self, account_number, amount):
        # Deposit money into the account
        if amount <= 0:
            return False  # Invalid deposit amount
        self.accounts[account_number]["balance"] += amount
        self.accounts[account_number]["transactions"].append(f"Deposited: ${amount}")
        return True

    def withdraw(self, account_number, amount):
        # Withdraw money from the account if sufficient balance is available
        if 0 < amount <= self.accounts[account_number]["balance"]:
            self.accounts[account_number]["balance"] -= amount
            self.accounts[account_number]["transactions"].append(f"Withdrew: ${amount}")
            return True
        return False

    def check_balance(self, account_number):
        # Return the current balance of the account
        return self.accounts[account_number]["balance"]

    def transaction_history(self, account_number):
        # Return the transaction history of the account
        return self.accounts[account_number]["transactions"]

    def transfer(self, from_account, to_account, amount):
        # Transfer money from one account to another
        if from_account in self.accounts and to_account in self.accounts:
            if self.withdraw(from_account, amount):
                self.deposit(to_account, amount)
                self.accounts[from_account]["transactions"].append(f"Transferred: ${amount} to {to_account}")
                self.accounts[to_account]["transactions"].append(f"Received: ${amount} from {from_account}")
                return True
        return False

    def update_pin(self, account_number, old_pin, new_pin):
        # Update the PIN for an account
        if self.authenticate(account_number, old_pin):
            self.accounts[account_number]["pin"] = new_pin
            return True
        return False

    def run(self):
        # Main loop for the ATM interface
        while True:
            print("\nWelcome to the ATM")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option (1-3): ")

            if choice == "1":
                account_number = input("Enter a new account number: ")
                pin = input("Set a 4-digit PIN: ")
                if self.create_account(account_number, pin):
                    print("Account created successfully!")
                else:
                    print("Account already exists! Please try a different account number.")

            elif choice == "2":
                account_number = input("Enter your account number: ")
                pin = input("Enter your PIN: ")
                if self.authenticate(account_number, pin):
                    print("Login successful! Welcome back!")
                    self.account_menu(account_number)
                else:
                    print("Invalid account number or PIN. Please try again.")

            elif choice == "3":
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option (1-3).")

    def account_menu(self, account_number):
        # Menu for account operations after login
        while True:
            print("\nAccount Menu")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transaction History")
            print("5. Transfer Funds")
            print("6. Update PIN")
            print("7. Logout")
            choice = input("Choose an option (1-7): ")

            if choice == "1":
                balance = self.check_balance(account_number)
                print(f"Your current balance is: ${balance:.2f}")

            elif choice == "2":
                amount = float(input("Enter the amount to deposit: "))
                if self.deposit(account_number, amount):
                    print("Deposit successful! Your new balance is: ${:.2f}".format(self.check_balance(account_number)))
                else:
                    print("Invalid amount. Please enter a positive value.")

            elif choice == "3":
                amount = float(input("Enter the amount to withdraw: "))
                if self.withdraw(account_number, amount):
                    print("Withdrawal successful! Your new balance is: ${:.2f}".format(self.check_balance(account_number)))
                else:
                    print("Insufficient balance or invalid amount. Please try again.")

            elif choice == "4":
                transactions = self.transaction_history(account_number)
                print("Transaction History:")
                if transactions:
                    for transaction in transactions:
                        print(transaction)
                else:
                    print("No transactions recorded yet.")

            elif choice == "5":
                to_account = input("Enter the account number to transfer to: ")
                amount = float(input("Enter the amount to transfer: "))
                if self.transfer(account_number, to_account, amount):
                    print("Transfer successful!")
                else:
                    print("Transfer failed. Please check the account number and balance.")

            elif choice == "6":
                old_pin = input("Enter your current PIN: ")
                new_pin = input("Enter your new PIN: ")
                if self.update_pin(account_number, old_pin, new_pin):
                    print("PIN updated successfully!")
                else:
                    print("Failed to update PIN. Please check your current PIN.")

            elif choice == "7":
                print("Logging out... Thank you for using the ATM!")
                break

            else:
                print("Invalid choice. Please select a valid option (1-7).")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
