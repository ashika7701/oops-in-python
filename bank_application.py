class bank_app:

    def __init__(self,account_holder,balance,account_number):
        self.account_holder=account_holder
        self.balance=balance
        self.account_number=account_number


    def deposit(self,amount):
        if(amount>0):
            self.balance+=amount
            return "sucessfully deposited"
        else:
            return "invaild amount"

        
    def withdraw(self,amount):
        if(amount>0):
            if(self.balance>=amount):
              self.balance-=amount
              return "sucesfully withdraw thank you"
            else:
                return "insufficient amount"
        else:
            return "INVAILD AMOUNT "

        
    

    def check_balance(self):
        return self.balance

    
    def transfer(self,reciver,amount):
        if amount > 0:
            if self.balance >= amount:
                if reciver is not self:
                    self.balance -= amount
                    reciver.balance += amount
                    return "sucessfully"
                else:
                    return "same sender/receiver"
            else:
                return "insufficeient amount"
        else:
            return "invalid amount"
        

             

def bankaccount(account):
 while(True):
    
    print("1. deposite")
    print("2. withdraw")
    print("3. transfer")
    print("4. choose_account")
    print("5. show details")
    print("6. check balance")
    print("7. exit")
    choice=int(input("enter your choice"))

    if choice == 1:
         amount1=int(input("enter deposite amount"))
         print(account.deposit(amount1))

    elif choice == 2:
     amount1=int(input("enter withdraw amount"))
     print(account.withdraw(amount1))

    elif choice == 3:
     sender=int(input("enter your sender account number"))
     reciver=int(input("enter your receiver acoount number"))
     if sender == ac1.account_number:
         sender=ac1
     elif sender == ac2.account_number:
         sender=ac2

     else:
         print("enter vaild number")
         continue
        
     if reciver == ac1.account_number:
         reciver=ac1
     elif reciver == ac2.account_number:
         reciver=ac2   
         
     else:
         print("enter vaild number")
         continue

     amount=int(input("enter amount"))
     print(sender.transfer(reciver,amount))

    elif choice == 4:
      choose_act=int(input("enter your account number"))
      if choose_act == ac1.account_number:
          account=ac1
      elif choose_act == ac2.account_number:
          account=ac2
      else:
         print("enter account number correctly")
          
 
         

    elif choice == 5:
     
     print("Account holder",account.account_holder)
     print("Account number",account.account_number)
     print("balance",account.balance)

    elif choice == 6:
     print(account.check_balance())

    elif choice == 7:
        break
    print("account balance",account.balance)

 

ac1=bank_app("ashika",5000,1001)
ac2=bank_app("nithya",7000,1002)

bankaccount(ac1)
