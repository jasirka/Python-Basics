from functools import reduce

# Lamba fn
# x = lambda a, b: a*b

# print(x(2,3))

#Map fn
# num_list = [2,3,6,7]

# sqrt_list = list(map(lambda x: x*x, num_list))
# print(sqrt_list)

# #Filter fn
# num_list = [3,4,6,8,7]

# even_list = list(filter(lambda n: n%2 == 0, num_list))
# print(even_list)

#Reduce fn
# Find maximum number from a list
# num_list = [12,23,56,27,78,54,67]
# max_num = reduce(lambda x,y: x if x > y else y, num_list)
# print(max_num)

#Find the sum of all numbers in a list
# sum_num = reduce(lambda x,y: x+y, num_list)
# print(sum_num)

# def sum_list(x, y):
#     return x+y

# sum_num = reduce(sum_list, num_list)
# print(sum_num)
