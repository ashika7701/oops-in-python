class Bank:
   def __init__(self,balance):
        self.balance=balance

class UPIPayment():
    def __init__(self,bank):
        self.bank=bank
    
    
    def pay(self,amount):
     if amount>0:
        if amount<=self.bank.balance:
          self.bank.balance-=amount
          return "paid",amount,"using UPI"
        else:
          return "insufficient amount"
     else:
       return "enter vaild amount"
    def check_balance(self):
            
            return self.bank.balance
    
          
           
class CardPayment(): 
  def __init__(self,bank):
          self.bank=bank
  
  
  def pay(self,amount):
       if amount>0:
          if amount<=self.bank.balance:
            self.bank.balance-=amount
            return "paid",amount,"using Card"
          else:
            return "insufficient amount"
       else:
         return "enter vaild amount"
  def check_balance(self):
          
          return self.bank.balance
   


class Cashpayment():
    def __init__(self,bank):
            self.bank=bank
    
    def pay(self,amount):
       if amount>0:
                   if amount<=self.bank.balance:
                     self.bank.balance-=amount
                     return "paid",amount,"using Cash"
                   else:
                     return "insufficient amount" 
       else:
                  return "enter vaild amount"
    def check_balance(self):
        
        return self.bank.balance
       
    
            
    
         
def payment(obj):
 
   am=int(input("enter AMOUNT"))
   print(obj.pay(am))
   print("BALANCE",obj.check_balance())
   
bank=Bank(50000)
upi=UPIPayment(bank)
card=CardPayment(bank)
cash=Cashpayment(bank)
payment(cash)
payment(upi)
payment(card)
