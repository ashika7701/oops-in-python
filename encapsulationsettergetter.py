class Student:
    def __init__(self,name):
        self.__name=name
    def hello(self):
        return self.__name
    def put_name(self,name1):
        self.__name=name1


st1=Student("ashika")
print(st1.hello()) 
st1.put_name("roshan")
print(st1.hello()) 

