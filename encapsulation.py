class Student:
    def __init__(self,mark):
        self.__mark=mark
    def get_marks(self):
        print("marks",self.__mark)
    def set_marks(self,new_marks):
        if new_marks >0 and new_marks<100:
            self.__mark=new_marks
            print("sucessfully added")
            print("your new mark will be",self.__mark)
        else:
            print("enter vaild mark")

st=Student(25)
st.get_marks()
st.set_marks(70)
