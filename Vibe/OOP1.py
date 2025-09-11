class Account:
    def __init__(self, balance, accountnumber):
        self.balance_amount = balance  # Renamed to avoid conflict
        self.accountnumber = accountnumber

    def debit(self, amount= None):
        if amount is None:
            amount = int(input("Enter the amount to be debited: "))
        if amount <= self.balance_amount:
            self.balance_amount -= amount
            print("Rs.",amount,"was debited to your account & Your balance is", self.balance_amount)
        else:
            print("Insufficient balance")
            print("Rs.",amount,"was debited to your account & Your balance is", self.balance_amount)
    
    def credit(self, amount=None):
        if amount is None:
            amount = int(input("Enter the amount to be credited: "))
        self.balance_amount += amount
        print("Rs.",amount,"was credited to your account & Your balance is", self.balance_amount)

    def get_balance(self):  # Renamed from balance() to avoid conflict
        print("Your balance is", self.balance_amount)

c1 = Account(10000, 2224082)
'''c1.credit(5000)
c1.debit(12500)'''
c1.get_balance()

