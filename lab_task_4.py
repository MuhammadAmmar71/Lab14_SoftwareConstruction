import threading
import random
import time

# Bank account class
class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    # Deposit method
    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited: {amount}, New Balance: {self.balance}")

    # Withdraw method
    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew: {amount}, New Balance: {self.balance}")
            else:
                print(f"Insufficient funds for withdrawal of: {amount}")

# Client thread function
def client_transactions(account):
    for _ in range(5):
        action = random.choice(["deposit", "withdraw"])
        amount = random.randint(10, 100)
        if action == "deposit":
            account.deposit(amount)
        else:
            account.withdraw(amount)
        time.sleep(0.1)  # Simulate delay between transactions

if __name__ == "__main__":
    account = BankAccount()

    # Create threads for multiple clients
    clients = [threading.Thread(target=client_transactions, args=(account,)) for _ in range(3)]

    # Start threads
    for client in clients:
        client.start()

    # Wait for threads to complete
    for client in clients:
        client.join()

    print(f"Final Balance: {account.balance}")
    print("Lab Task 4 completed!")
