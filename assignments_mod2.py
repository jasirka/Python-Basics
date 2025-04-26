#program to create a list of 5 numbers and print the sum and average. (hint:Use Sum Built In Function)
# nums = [24,67,32,56,47]
# sum = sum(nums)
# print("Sum of the numbers = ", sum)

# average = sum / 5
# print("Average of the numbers = ", average)

# #Program to remove all even numbers from a list.
# num_list = [23,36,68,33,87,24,90,35,18]
# new_list = []
# for num in num_list:
#     if num%2 != 0:
#         new_list.append(num)

# print(new_list)

# #Program to find the second largest number in a list.
# num_list = [23,36,68,33,87,24,90,35,18]
# num_list.sort()
# # print(num_list)
# print(num_list[len(num_list) - 2])

# #program to merge two lists and remove duplicates.
# list1 = [4,5,7,2,3]
# list2 = [1,3,9,6]
# merged_list = list1 + list2
# print(merged_list)

# new_set = set(merged_list)
# print(new_set)

# #program to replace every negative number in a list with 0.
# list = [4,-7,3,8,-2,6,8]

# i=0
# while(i < len(list)):
#     if list[i] < 0:
#         list[i] = 0
#     i+=1
# print(list)

# #program to find all the unique elements in a list.
# # nlist = [5,2,3,7,2,5,8,1,7,9]
# # ulist = []
# # for num in nlist:
# #     if num not in ulist:
# #         ulist.append(num)
# # print(ulist)                    # list after removing all duplicates

# unique_num = [n for n in nlist if nlist.count(n) == 1]
# print(unique_num)                # unique elements in the list

# #program to create a tuple with values of different data types and print its length.
# test_tuple = ("hii", 100, ["BMW", 2017])
# print(len(test_tuple))

# #program to count the occurrence of a particular element in a tuple.
# tuple_car = ("BMW", "Red", "BMW", 2017)
# print(tuple_car.count("BMW"))

# #program to concatenate two tuples and sort them.
# tuple_1 = (12, 54, 65, 23)
# tuple_2 = (25, 46, 74, 48)
# tuple_s = tuple_1 + tuple_2
# list_s = list(tuple_s)
# list_s.sort()
# tuple_s = tuple(list_s)
# print(tuple_s)

# #program to create a dictionary of 5 students with name as key and marks as value
# dict_stud = {"Ashik": 47, "John": 50, "Benny": 56, "Tom": 68}
# print(dict_stud)

# #program to find the student(s) with the highest mark.
# dict_stud = {45: "Ashik", 50: "John", 56: "Benny", 37: "Tom"}
# max_mark = max(dict_stud.keys())
# print(dict_stud.get(max_mark))

# #program to merge two dictionaries. If same keys exist, sum the values.
# dict_1 = {"Ashik": 54, "Jinu": 67, "Benny": 78}
# dict_2 = {"Tom": 65, "Ashik": 46, "Basil": 53}

# merged_dict = dict_1.copy()
# for key,value in dict_2.items():
#     if key in merged_dict:
#         merged_dict[key]+=value
#     else:
#         merged_dict[key]=value
# print(merged_dict)

#program to delete a key from a dictionary if it exists.
# dict_car = {"name":"Suzuki Ciaz","Modal": "VX", "Year":"2017"}
# name = dict_car.pop("name")
# print(dict_car)
# print(name)

#program to group words with the same length using dictionary.
# words = ["apple", "banana", "kiwi", "lemon", "mango"]

# same_group = {}
# for word in words:
#     length = len(word)
#     if length in same_group:
#         same_group[length].append(word)
#     else:
#         same_group[length]=[word]

# for key,value in same_group.items():
#     print(f"length {key}:{value}")

#program to create two sets and perform union, intersection, and difference.
# fruits = {"apple","mango","orange", "cauliflower"}
# vegetables = {"onion","beans","cauliflower"}
# un_items = fruits.union(vegetables)
# # print(un_items)

# in_items = fruits.intersection(vegetables)
# # print(in_items)

# df_items = fruits.difference(vegetables)
# print(df_items)

#program to remove duplicates from a list using set.
# veh_list = ["Benz C class", "Porche", "Benz C class", "Tata Altroz XZ", "Suzuki Ciaz"]
# veh_set = set(veh_list)
# veh_list = list(veh_set)
# print(veh_list)

#program to find common elements in three sets.
# set_1 = {"item_1", "item_2", "item_3"}
# set_2 = {"item_2", "item_4", "item_3"}
# set_3 = {"item_3", "item_2", "item_6"}

# set_all = set_1 & set_2 & set_3

# print(set_all)

#program to convert a list to a set and sort it in ascending order.
# num_list = [4, 7, 2, 6, 8, 1, 5]
# num_list.sort()
# num_set = set(num_list)
# print(num_set)

#program to find the symmetric difference between two sets.
# set_1 = {2, 3, 5, 6}
# set_2 = {3, 5, 7, 8}
# set_sym_diff = set_1.symmetric_difference(set_2)
# print(set_sym_diff)

#program to count the frequency of each character in a string using a dictionary.
str_1 = "welcome"
for s in str_1:
    print(f" count of {s}", str_1.count(s))

