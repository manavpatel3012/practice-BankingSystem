class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance

    def get_balance(self):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

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

    