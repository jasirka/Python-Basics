# class Student:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
  
#         # print(f"Gross percentage: {self.gross_percentage}")


# class Evaluation(Student):
#     def __init__(self,fname,lname,age):
#         self.age=age
#         self.firstname=fname
#         self.lastname=lname
#     def show_details(self):
#         print("Name of the student", self.firstname,self.lastname,self.age)

  
# # stud = Student("Akhil", "Maraar")
# # stud.show_details()

# stud1=Evaluation("anju","david",23) 
# stud1.show_details()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, age):
    super().__init__(fname, lname)
    self.age = age
  
  def printage(self):
    print(self.age)

x = Student("Mike", "Olsen", 23)
x.printname()
x.printage()