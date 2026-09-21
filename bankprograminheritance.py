class BankAccount:
  def __init__(self,account_holder,balance):
    self.account_holder=account_holder
    self.balance=balance
  def display_details(self):
    print("Name",self.account_holder)
    print("balance",self.balance)
  def withdraw(self,amount):
    
      self.balance-=amount
      print("new balance:",self.balance)
  def deposit(self,amount):
    self.balance+=amount
    print("Deposited:", amount)
    print("New Balance:", self.balance)
      
    
class SavingsAccount(BankAccount):
  def __init__(self,account_holder, balance,interest_rate):
    super().__init__(account_holder,balance)
    self.interest_rate=interest_rate
  def calculate_interest(self):
    interest=self.balance*(self.interest_rate/100)
    print("interest",interest)
class CurrentAccount(BankAccount):
  def __init__(self,account_holder,balance):
   super().__init__(account_holder,balance)
  
  def withdraw(self,amount):
    if amount<=self.balance:
      self.balance-=amount
      print("sucessfully withdraw")
    else:
        print("insufficient amount")
s = SavingsAccount("Arun", 10000, 5)

s.display_details()
s.calculate_interest()
s.withdraw(2000)
s.deposit(3000)

print("Balance after withdrawal:", s.balance)


# Create a CurrentAccount object
c = CurrentAccount("Rahul", 5000)

c.display_details()
c.withdraw(6000)
  
