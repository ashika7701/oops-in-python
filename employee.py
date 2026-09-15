class employee:
    def __init__(self,employee_name,employee_id,salary):
        self.name=employee_name
        self.employee_id=employee_id
        self.salary=salary
        self.annual_salary=self.annual_salary
    def annual_salary(self):
        self.annual_salary=self.salary*12
    def display_details(self):
        print("name:",self.name,"\nEMP ID",self.employee_id,"\n Monthly salary",self.salary,"\nAnnual incomr",self.annual_salary)
emp1=employee("ashika",650,20000)
emp1.annual_salary()
emp1.display_details()
    