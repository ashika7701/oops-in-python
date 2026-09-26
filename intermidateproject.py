#it is an intermidiate level programming
#Empolyee salary
from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,id):
        self.__name=name
        self.__id=id
        
    def put_details(self,__.name,__id):
        return self.__name,self.__id
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self,__name,__id,monthlysalary,bonus):
        super().__init__(__name,__id)
        self.monthlysalary=monthlysalary
        self.bonus=bonus
    def calculate_salary(self):
        print("employee name",self.__name)
        print("employee id",self.__id)
        print("monthly salary",self.monthlysalary+self.bonus)
class PartTimeEmployee(Employee):
    def __init__(self,__name,__id,hoursworked,hourlyrate):
        super().__init__(__name,__id)
        self.hoursworked=hoursworked
        self.hourlyrate=hourlyrate
    def calculate_salary(self,):
        print("employee name",self.__name)
        print("employee id",self.__id)
        print("monthly salary",self.hoursworked+self.hourlyrate)
emp1=FullTimeEmployee("Ashika",101,3000,5000)
emp2=PartTimeEmployee("roshan",102,80,250)
print(emp1.name)
print(emp1.id)
print(emp1.calculate_salary())
    

        
    
        
