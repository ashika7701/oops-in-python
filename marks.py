class Student_marks:

    def __init__(self, student_name, roll_no, tamil_mark, english_mark,
                 science_mark, social_mark, math_mark):

        self.student_name = student_name
        self.roll_no = roll_no
        self.tamil_mark = tamil_mark
        self.english_mark = english_mark
        self.science_mark = science_mark
        self.social_mark = social_mark
        self.math_mark = math_mark

    def total(self):
        return (self.tamil_mark + self.english_mark +
                self.science_mark + self.social_mark +
                self.math_mark)

    def average(self):
        return self.total() / 5

    def result(self):
        if self.average() >= 50:
            return "PASS"
        else:
            return "FAIL"

    def show_details(self):
        print("Name:", self.student_name)
        print("Student Roll No:", self.roll_no)
        print("Tamil Mark:", self.tamil_mark)
        print("English Mark:", self.english_mark)
        print("Science Mark:", self.science_mark)
        print("Social Mark:", self.social_mark)
        print("Math Mark:", self.math_mark)

        print("Total:", self.total())
        print("Average:", self.average())
        print("Result:", self.result())


# Creating object
stud1 = Student_marks("Ashika", 650, 98, 56, 79, 86, 72)

# Display details
stud1.show_details()