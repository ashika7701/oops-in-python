
class Employee:
  def __init__(self,name,salary):
     self.name=name
     self.salary=salary
  def display_details(self):
    print("Name",self.name)
    print("salary",self.salary)
  def calculate_bonus(self):
    bonus = self.salary * 10 / 100
    print("bonus amount",bonus)
  
class Manager(Employee):
  def __init__(self,name,salary,team_size):
    super().__init__(name,salary)
    self.team_size=team_size
  def calculate_bonus(self):
    bonus = self.salary * 20 / 100
    print("bonus amount",bonus)
class Developer(Employee):
  def __init__(self,name,salary,programming_language):
    super().__init__(name,salary)
    self.programming_language=programming_language
  def calculate_bonus(self):
    bonus = self.salary * 15 / 100
    print("bonus amount",bonus)
m = Manager("Arun", 50000, 10)
m.display_details()
m.calculate_bonus()

d = Developer("Rahul", 40000, "Python")
d.display_details()
d.calculate_bonus()
