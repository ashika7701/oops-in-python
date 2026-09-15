class Bank_Account:
    def __init__(self,Account_Holder,balance):
        self.Account_Holder=Account_Holder
        self.balance=balance
    def deposite(self,deposite):
        self.balance=self.balance+deposite
    def widhdraw(self,widhdraw):
        if(self.balance>widhdraw):
         self.balance=self.balance-widhdraw
        else:
           print("insufficient amount")
    def account_balance(self):
       print("your current account balance:",self.balance)
acc1=Bank_Account("Ashika",1000)
acc2=Bank_Account("Roshan",7000)
acc1.deposite(1000)
acc1.account_balance()

acc2.widhdraw(2000)
acc2.account_balance()
acc1.widhdraw(4000)
acc1.account_balance()