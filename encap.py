# Online Python compiler (interpreter)
# Write and run Python online using this editor.

class BankAccount:
  def __init__(self,balance,pin):
    self.__balance=balance
    self.__pin=pin

    
  def deposit(self,amount,userpin):
   if(userpin==self.__pin):
    if amount>0:
      self.__balance+=amount
      print("deposited",amount)
    else:
      print("enter vaild amount")
   else:
    print("enter vaild pin no")
  
  def withdraw(self,amount,userpin):
   
   
   if(userpin==self.__pin):
     if amount>0:
     
        if amount<=self.__balance:
         self.__balance-=amount
         print("widthdraw",amount)
        else:
         print("insufficient balance")
       
     
   
     else:
     
       print("amount must be positive")
   else:
      print("enter vaild pin")
  def get_balance(self,userpin):
    if(userpin==self.__pin):
    
      print("balance",self.__balance)
    else:
      print("enter vaild pin")
a1=BankAccount(1000,2004)
userpin=int(input("enter your pin number"))
a1.deposit(500,userpin)
a1.withdraw(300,userpin)
a1.get_balance(userpin)
