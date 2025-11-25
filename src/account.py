class Account:
    def __init__(self, owner, pin, balance=0.0, history=None):
        self.owner = owner
        self.pin = pin
        self.balance = balance
        self.history = history if history else []

    def check_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Jumlah deposit harus lebih dari 0")
        self.balance += amount
        self.history.append(f"Deposit: +{amount}")
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Jumlah withdraw harus lebih dari 0")
        if amount > self.balance:
            raise ValueError("Saldo tidak cukup")
        self.balance -= amount
        self.history.append(f"Withdraw: -{amount}")
        return self.balance
