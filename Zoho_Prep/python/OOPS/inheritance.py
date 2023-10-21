class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_details(self):
        person_details = super().get_details()
        return f"{person_details}, Student ID: {self.student_id}"

person = Person("Alice", 30)

student = Student("Bob", 20, "12345")

print("Person:")
print(person.get_details())

print("\nStudent:")
print(student.get_details())
