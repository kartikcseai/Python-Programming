# Description: A simple banking system that allows users to create bank accounts, deposit money, withdraw money, and check their balance.

class BankAccount:
    def __init__(self, initial_deposit):
        self.balance = initial_deposit

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds for withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. Current Balance: {self.balance}")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

# Example usage
account = BankAccount(100)  # Create an account with an initial deposit of 100
account.deposit(50)         # Deposit money
account.withdraw(30)        # Withdraw money
account.check_balance()      # Check balance