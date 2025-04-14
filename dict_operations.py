dict_emp = {"name": "Ashik", "age": 35, "Designation": "IT Support"}
dict_emp = dict("name": "Ashik", "age": 35, "Designation": "IT Support") # alternate way
print(len(dict_emp))

if "age" in dict_emp:
    print("Age of the employee is available")

print(dict_emp["name"])

print(dict_emp.get("name"))

for key in dict_emp.keys():
    print(key)

for value in dict_emp.values():
    print(value)

for key,value in dict_emp.items():
    print(key, value)


items = dict_emp.items()
print(items)

dict_emp["Date of join"] = "04/06/2019"   # Add new item to the dictionary
print(dict_emp)

dict_emp.update({"Designation": "IT Support Engineer"})
print(dict_emp)

dict_emp.pop("Date of join")
print(dict_emp)

dict_emp.popitem()   # Removes the last inserted item
print(dict_emp)

dict_emp.clear()
print(dict_emp)

del dict_emp
print(dict_emp)