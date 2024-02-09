class BankAccount:
    def __init__(self, owner, initial_balance = 0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"The {amount} deposit has been successfully completed. New balance: {self.balance}")
        else:
            print("The deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawal completed successfully. New balance: {self.balance}")
        else:
            print("Error: Insufficient funds or incorrect withdrawal amount.")

account = BankAccount(owner = "Azim", initial_balance = 0)

account.deposit(100)
account.withdraw(187)
account.deposit(444)
account.withdraw(500)