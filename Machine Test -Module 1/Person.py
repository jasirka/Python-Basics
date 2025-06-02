class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def print_student_details(self):
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Marks: ', self.marks)
        
student = Student("Ajith",27,50)
student.print_student_details()
