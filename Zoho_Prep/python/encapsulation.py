class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.rollno = roll_no
        self.grade = {}
    
    def set_grade(self, subject, grade):
        if subject not in self.grade:
            self.grade[subject] = grade
        
    def get_grade(self, subject):
        if subject in self.grade:
            return self.grade[subject]
        else:
            return "No Grade"
        
    def get_name(self):
        return self.name

    def get_rollno(self):
        return self.rollno
    
    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No.: {self.rollno}")
        print("Grades:")
        for subject, grade in self.grade.items():
            print(f"{subject} : {grade}")

student1 = Student("Ram", "123")
student1.set_grade("Maths", 100)
student1.set_grade("Science", 100)

student1.print_info()