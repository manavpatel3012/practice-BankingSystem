class BankAccount:
    def __init__(self, account_holder, initial_balance):
        if not account_holder:
            raise ValueError("Account holder name cannot be empty.")
        
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        
        self.account_holder = account_holder
        self.balance = initial_balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

class BankingApp:
    def __init__(self, account):
        self.account = account

    def show_menu(self):
        print("\nBanking App Menu:")
        print("1. View Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                print(f"Your balance is: ${self.account.get_balance()}")
            elif choice == "2":
                amount = self.get_amount_input("Enter deposit amount: ")
                if amount is not None:
                    self.account.deposit(amount)
                    print("Deposit successful.")
            elif choice == "3":
                amount = self.get_amount_input("Enter withdrawal amount: ")
                if amount is not None:
                    self.account.withdraw(amount)
                    print("Withdrawal successful.")
            elif choice == "4":
                print("Thank you for using the Banking App.")
                break
            else:
                print("Invalid choice. Please try again.")

    def get_amount_input(self, prompt):
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return None

def main():
    account = BankAccount("John Doe", 1000)
    app = BankingApp(account)
    app.run()

if __name__ == "__main__":
    main()

    