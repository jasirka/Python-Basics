test_set = {"apple", "orange", "banana"}
test_set.add("kiwi")

for item in test_set:
    print(item)

print("banana" in test_set) # check if banana is present in test_set

print("banana" not in test_set) # check if banana is not present in test_set

new_set = {"lemon", "pine apple"}
test_set.update(new_set)

test_set.pop() # remove element randomly

test_set.clear()

test_set.remove("kiwi")  # will raise error if element is not found

test_set.discard("banana") # will get -1 if element is not found

del test_set

set1 = {67, 78, 34}
set2 = {55, 65, 76}
set3 = {56, 43, 67}

set4 = set1.union(set2)
set5 = set1 | set2 # Another form of set union

set6 = set1.union(set2, set3)
set6 = set1 | set2 | set3 # Another form of set union

y = (65,67,78)
set7 = set1.union(y)

set1.update(set2) # Inserts the items in set2 to set1

# Both union() and update() will exclude any duplicate items.








