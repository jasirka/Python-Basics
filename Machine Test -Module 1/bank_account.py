class Bank_Account():
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        self.__balance = self.__balance - amount

    def get_balance(self):
        return self.__balance

bank_account = Bank_Account(5000)
print(f'Initial balance = {bank_account.get_balance()}')

bank_account.deposit(3000)
print(f'After depositing 3000, the new balance is {bank_account.get_balance()}')

bank_account.withdraw(1000)
print(f'After withdrawing 1000, the new balance is {bank_account.get_balance()}')
