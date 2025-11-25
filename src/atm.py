import json
import os
from .account import Account

DATA_FILE = "data/accounts.json"

class ATM:
    def __init__(self):
        self.accounts = self.load_data()

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return {}

        with open(DATA_FILE, "r") as f:
            raw = json.load(f)

        accounts = {}
        for owner, data in raw.items():
            accounts[owner] = Account(
                owner,
                data["pin"],
                data["balance"],
                data["history"]
            )
        return accounts

    def save_data(self):
        data = {}
        for owner, acc in self.accounts.items():
            data[owner] = {
                "pin": acc.pin,
                "balance": acc.balance,
                "history": acc.history,
            }

        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def create_account(self, owner, pin, balance=0):
        if owner in self.accounts:
            raise ValueError("Akun sudah ada!")

        self.accounts[owner] = Account(owner, pin, balance)
        self.save_data()
        return self.accounts[owner]

    def authenticate(self, owner, pin):
        if owner not in self.accounts:
            raise ValueError("Akun tidak ditemukan")
        acc = self.accounts[owner]
        if not acc.check_pin(pin):
            raise ValueError("PIN salah")
        return acc

    def deposit(self, owner, pin, amount):
        acc = self.authenticate(owner, pin)
        new_balance = acc.deposit(amount)
        self.save_data()
        return new_balance

    def withdraw(self, owner, pin, amount):
        acc = self.authenticate(owner, pin)
        new_balance = acc.withdraw(amount)
        self.save_data()
        return new_balance

    def check_balance(self, owner, pin):
        acc = self.authenticate(owner, pin)
        return acc.balance

    def get_history(self, owner, pin):
        acc = self.authenticate(owner, pin)
        return acc.history
