class teacher:
  def __init__(self,name):
    self.name=name
  def allocate(self,s1):
    print(self.name,"is taking class for ",s1.student_name)
    
class student:
  def __init__(self,student_name):
    self.student_name=student_name


t1=teacher("sharmi")
s1=student("ashika")
t1.allocate(s1)