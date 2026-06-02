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
        pass

    def show_menu(self):
        pass

    def run(self):
        pass

    def get_amount_input(self, prompt):
        pass

def main():
    account = BankAccount("John Doe", 1000)
    app = BankingApp(account)
    app.run()

if __name__ == "__main__":
    main()

    