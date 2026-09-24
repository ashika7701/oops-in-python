
class ATM:
    def __init__(self,pin1):
        self.__pin1=pin1
    def check_pin(self,userpin):
        
        if userpin==self.__pin1:
            return True
        else:
            return False
    def change_pin(self,old_pin):
        if old_pin==self.__pin1:
            return True
        else:
            return "INVAILD PIN"
        
        
class BankAccount:
    
    def __init__(self,balance):
        self.__balance=balance
    def deposite(self,amount):
        

        
        if amount>0:
            self.__balance +=amount
            return("sucessfully deposited")
        else:
            return "invaild amount"
    def widthdraw(self,amount):
        

        if amount>0:
            if amount<=self.__balance:
              self.__balance-=amount
              return "sucessfully withdrawl"
            else: 
                return "insufficient amount"
        else:
            return " invaild amount"
    def get_balance(self):
        return self.__balance
    
def account_action(obj,obj1):
    while(1):
        print("welcome")
        print("1. deposite")
        print("2. widthdraw")
        print("3. check_balance")
        print("4. end")
        choice=int(input("enter choice"))
        if(choice==1):
            user_pin=int(input("enter your pin"))
            result=obj1.check_pin(user_pin)
            if result == True:
                print("CORRECT PIN")
                am=int(input("enter amount"))
                print(obj.deposite(am))
            else:
                print("INVAILD PIN")
           
        elif(choice==2):

           user_pin=int(input("enter your pin"))
           result=obj1.check_pin(user_pin)
           if result:
                print("CORRECT PIN")
                am=int(input("enter amount"))
                print(obj.widthdraw(am))
           else:
                print("INVAILD PIN")

        elif(choice==3):
            user_pin=int(input("enter your pin"))
            result=obj1.check_pin(user_pin)
            if result:
                print("CORRECT PIN")
                
                print(obj.get_balance())
            else:
                 print("INVAILD PIN")

        elif(choice==4):
            oldpas=int(input("enter old password"))
            
            result=obj1.change_pin(oldpas)
            if result:
                newpas=int(input("enter new password"))
                obj1.change_pin(newpas)

            
        elif(choice==4):
            print("thank you!")
            break
A=ATM(1004)
b1=BankAccount(50000)
account_action(b1,A)


