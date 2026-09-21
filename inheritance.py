class person:
  def __init__(self,name):
    self.name=name
  def display_name(self):
    print("name:",self.name)
class Student(person):
  def __init__(self,name,course):
    super().__init__(name)
    self.course=course
  def display_course(self):
    print("course name",self.course)
s = Student("Arun", "Python")

s.display_name()
s.display_course()
