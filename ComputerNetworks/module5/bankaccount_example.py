import threading
from random import randint


class BankAccount:
    def __init__(self, initialmoney=0) -> None:
        self.balance = initialmoney
        self.lock = threading.Lock()

    def withdraw(self, amount):
        with self.lock:
            if self.balance <= 0 or self.balance-amount < 0:
                print("You do not have that much money\n")
            else:
                self.balance -= amount
                print("Withdrawn {}\n".format(amount))
        self.checkAvailable()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print("Deposited {}\n".format(amount))
        self.checkAvailable()

    def checkAvailable(self):
        with self.lock:
            print("Available {}\n".format(self.balance))


class DepositThread(threading.Thread):
    def __init__(self, account_name, value):
        threading.Thread.__init__(self)
        self.bankaccount = account_name
        self.amount = value

    def run(self):
        self.bankaccount.deposit(self.amount)


class WithdrawThread(threading.Thread):
    def __init__(self, account_name, value):
        threading.Thread.__init__(self)
        self.bankaccount = account_name
        self.amount = value

    def run(self):
        self.bankaccount.withdraw(self.amount)


def main():
    account = BankAccount(100)
    print("Bank Account created\n")
    account.checkAvailable()
    t1 = DepositThread(account, 30)
    t1.start()
    t2 = DepositThread(account, 20)
    t2.start()
    t3 = DepositThread(account, 10)
    t3.start()
    t4 = WithdrawThread(account, 30)
    t4.start()
    t5 = WithdrawThread(account, 50)
    t5.start()
    t6 = WithdrawThread(account, 20)
    t6.start()
    account.checkAvailable()


# Call the main fucntion only if the file has not been
# imported into another program
if __name__ == "__main__":
    main()
