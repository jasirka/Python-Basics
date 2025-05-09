# Create a class Car that has attributes like make, model, and year. Include methods to:
# • Display car details
# • Start and stop the car (change a status attribute between "Started" and "Stopped").
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display_car_details(self):
        print(f"Car details: {self.make} {self.model} {self.year}")

    def start_car(self):
        print(f"{self.make} {self.model} is started")

    def stop_car(self):
        print(f"{self.make} {self.model} is stopped")

c = Car("Suzuki","Ritz",2011)
c.display_car_details()
c.start_car()
c.stop_car()

# Create a base class Shape with a method area(). Then, create subclasses Rectangle,Circle, and Triangle,
# each with its own area() method implementation. Demonstrate polymorphism by creating a list of Shape objects
# and calculating their areas dynamically.
import math
class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        self.area = self.length * self.width
        return self.area
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        self.area = math.pi * math.pow(self.radius,2)
        return self.area

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        self.area = 1/2 * (self.base * self.height)
        return self.area
    
shape = Shape()
shape.area()
rect = Rectangle(2,3)
rect_area = rect.area()
cir = Circle(4)
cir_area = cir.area()
tri = Triangle(5,4)
tri_area = tri.area()

option = int(input("Please provide the option \n Press 1: Calculate area of the rectangle \n Press 2: Calculate are of the Circle \n Press 3: Calculate are of the triangle\n"))
match(option):
    case 1: print(f"Area of rectangle= {rect_area}")
    case 2: print(f"Area of circle= {cir_area}")
    case 3: print(f"Area of triangle= {tri_area}")

# Create a Bank class with methods to open new accounts, deposit money, and withdraw money.
# The BankAccount class should have attributes like account_number, balance, and a method to display the account balance.

class Bank:
    def __init__(self):
        pass
    def open_new_account(self):
        print("New account is created")
    def deposit_money(self):
        print("Money is deposited on the new account")
    def withdraw_money(self):
        print("Money is withdrawed from the new account")

class BankAccount(Bank):
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def display_account_balance(self):
        print(f"Balance for the account no: {self.acc_no} : {self.balance}")

bank = BankAccount("23512466","50000")
bank.open_new_account()
bank.deposit_money()
bank.withdraw_money()
bank.display_account_balance()

# Define an abstract class Animal with two abstract methods: make_sound() and move().Then, create subclasses Dog and Fish.
# The Dog class should implement the make_sound() method to print "Woof!" and the move() method to print "Running". 
# The Fish class should implement make_sound() as "Blub!" and move() as "Swimming".

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")
        
    def move(self):
        print("Running")

class Fish(Animal):
    def make_sound(self):
        print("Blub!")
        
    def move(self):
        print("Swimming")
    
dog = Dog()
dog.make_sound()
dog.move()

fish = Fish()
fish.make_sound()
fish.move()

#Define a class Calculator with a method add(). Overload this method so that it can accept either two integers or 
# three integers and return their sum. Create instances and test the method.

class Calculator:
    def __init__(self):
        pass
    
    def add(self, num1, num2, num3=0):
        self.sum = num1 + num2 + num3
        return self.sum
    
calc = Calculator()
print(f"Sum of the 2 numbers = {calc.add(3,7)}")
print(f"Sum of the 3 numbers = {calc.add(3,7,5)}")







