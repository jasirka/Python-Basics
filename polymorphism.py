# === Method Overloading ===

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print(f"{self.brand} {self.model} -- Drive!")

# class Boat:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print(f"{self.brand} {self.model} -- Sail!")

# class Plane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print(f"{self.brand} {self.model} -- Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#     x.move()

# === Method Overriding ===

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Move!")

# class Car(Vehicle):
#     pass
#     # def move(self):
#     #     # print("Moving Car!")

# class Boat(Vehicle):
#     def move(self):
#         print("Sailing Boat!")

# class Plane(Vehicle):
#     def move(self):
#         print("Flying Plane!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#     print(f"{x.brand} \t {x.model}")
#     x.move()



# === Method Overloading Exception Case ===

class Car:
    def __init__(self):
        pass

    # def move(self):
    #     print("Drive!")       # This will not work since for same class arguments cannot be empty.

    def move(self, brand):
        print(f"{brand} -- Drive!")

car1 = Car()       #Create a Car object
car1.move("Benz")
# car1.move()  # This will not work since for same class arguments cannot be empty.

# to resolve the issue pass default arguements with the base method
car1.move(brand="")