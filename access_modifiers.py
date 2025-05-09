# Private variables can be accessed only inside the class. In order to access the private variables outside the class, 
# it should define public function inside the class. then access that public method.
# __ is used to define private variables. _ is used to define protected variables. Normal variables are public by default.

class Person:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def get_details(self):  # Allowed to access private variables through public function
        print(f"Name: {self.__name}")
        print(f"Address: {self.__address}")

    def __get_details(self): # Not alowed to access private variables through private function
        print(f"Name: {self.__name}")
        print(f"Address: {self.__address}")

p = Person("Raj","Kochi")
p.get_details()

# Real world Example
class Hospital:
    def __init__(self):
        self.hospital_name = "ABC"   # public 
        self._staff_code = "16547"   # protected
        self.__admin_code = "54367"  # private
    
    def _get_hopital_info(self):
        print(f"Hospital name: {self.hospital_name}")

class Doctor(Hospital):
    def __init__(self):
        super().__init__()

    def get_info(self):
        print(f"Staff code: {self._staff_code}")
        # print(f"Admin code: {self.__admin_code}")  # Will through error since admin code is private

doctor = Doctor()
doctor._get_hopital_info()
doctor.get_info()
    


