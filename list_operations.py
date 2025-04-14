list1=[34,"hello",7.88,45,99,"python",666.9]
print(list1)
print(type(list1))

print(list1[1])
print(list1[1:3])
print(list1[::-1])


#change elements
list1[2]=8.88
print(list1)

list1.insert(1, "welcome")
print(list1)
list2 = [45,78,"hii"]
list1.extend(list2)
print(list1)
# list3=list1+list2
# print(list3)

# list1.remove("hii")
list1.pop(1)
print(list1)
# list3.clear()
# print(list3)
# del list3
# print(list3)

# list1.append(77)
# print(list1)

# print(list1.index("hii"))
# my_list = [45,12,76,56,23]
# my_list.sort()
# print(my_list)

# [x for x in my_list if x > 23]

# for i in range(len(list1)):
#     print(list1[i])
x1 = [23,76,34,78,98,15,27,35,99]
x1.sort(reverse=True)
# x2 = [x for x in x1 if x < 35]
# print(x2)
# print(x1)

x1_copy = x1.copy()
# print(x1_copy)
# x3 = x1[:]
# print(x3)
x4 = list(x1)
print(x4)