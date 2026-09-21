class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  def display_employee(self):
    print("Name",self.name)
    print("salary",self.salary)
class Developer(Employee):
  def __init__(self,name,salary,language):
    super().__init__(name,salary)
    self.language=language
  def display_developer(self):
    print("language",self.language)
d = Developer("Arun", 30000, "Python")

d.display_employee()
d.display_developer()
