class docter:
  def __init__(self,docter_name):
    self.docter_name=docter_name
  def treat(self,p1):
    print(self.docter_name, "is treating",p1.patient_name)
class patient:
  def __init__(self,patient_name):
    self.patient_name=patient_name
d1=docter("ramesh")
p1=patient("suresh")
d1.treat(p1)