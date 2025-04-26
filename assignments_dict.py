# #Create a dictionary representing a person (e.g., name, age). Then, add a new key-value pair to the dictionary representing the person’s email.
# dict_person = {"name": "xxx", "age": "27"}
# dict_person.update({"email":"xxx@yopmail.com"})
# print(dict_person)
# #Given a dictionary, check if a certain key exists in the dictionary and print "Found" or "Not Found" accordingly.
# products = {'laptop': 1000, 'phone': 600, 'tablet': 300}
# for key in products.keys():
#     flag = False
#     if key == "laptop":
#         flag = True
#         break
# if flag == True:
#     print("Found")
# else:
#     print("Not Found")
#Create a dictionary and remove a key-value pair from it. After removal, print the dictionary.
# dict_employee = {"name": "RX", "age": "27", "phone": "555555", "email":"rx100@ymail.com","department":"Devteam"}
# print(f"== Before remove the key 'department' from the employee dictionary == \n{dict_employee} ==")
# dict_employee.pop("department")
# print(f"== After removed the key 'department' from the employee dictionary == \n{dict_employee}")
#Given two dictionaries, merge them into one dictionary. If both dictionaries have the same key, the value from the second dictionary should overwrite the value in the first dictionary.
# dict_p = {"id": "123", "name": "JK", "age": "35"}
# dict_d = {"id":"124" ,"designation": "Accounting"}
# dict_p.update(dict_d)
# print(dict_p)
#Create a dictionary with numerical values and find the maximum and minimum values, along with their corresponding keys.
# emp_salary = {"Abin": 5000, "Ajas": 10000, "Ebin": 25000, "Albin": 15000}
# print(min(emp_salary.values()))
# print(max(emp_salary.values()))
#Create a dictionary that maps integers (1 to 5) to their squares using dictionary comprehension.
# dict_sqrt = {x:x**2 for x in range(1, 6)}
# print(dict_sqrt)
#Given a dictionary of student grades, filter the students who have a grade above 80. 
# grades = {'Alice': 85, 'Bob': 78, 'Charlie': 92, 'David': 65}
# for student, grade in grades.items():
#     if grade > 80:
#         print(f"{student} : {grade}")
#Given a dictionary of employee salaries, increase the salary by 10% for all employees whose salary is less than 50,000.
# Emp_salaries = {'Alice': 45000, 'Bob': 60000, 'Charlie': 40000}
# print(f"==  Employee salary dictionary before the salary increment == \n{Emp_salaries}")
# for emplyeee, salary in Emp_salaries.items():
#     if salary < 50000:
#         new_salary = salary + (salary * 10)/100
#         Emp_salaries.update({emplyeee:new_salary})
# print(f"==  Employee salary dictionary after increasing the salary by 10% for all employees whose salary is less than 50,000.  == \n{Emp_salaries}")

#Given a list of tuples where each tuple contains a key-value pair, convert the list into a dictionary.
# tuple_list = [('a', 1), ('b', 2), ('c', 3)]
# print(dict(tuple_list))
#You are given a list of dictionaries, where each dictionary contains a person's name and age. Group the people into categories based on their age groups (e.g., "Teen", "Adult", "Senior").
people = [
{'name': 'Alice', 'age': 15},
{'name': 'Bob', 'age': 25},
{'name': 'Charlie', 'age': 35},
{'name': 'David', 'age': 55},
{'name': 'Eve', 'age': 75}
]

for person in people:
    age = person.get("age")
    if age < 18:
        person["category"] = "Teen"
    elif 18 <= age < 60:
        person["category"] = "Adult"
    else:
        person["category"] = "Senior"

# Print the results
for person in people:
    print(f"{person['name']} | {person['age']} | {person['category']}")