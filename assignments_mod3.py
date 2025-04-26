#program to define a function that can accept an integer number as input and print the "It is an even number" if the
# number is even, otherwise print "It is odd".
# num = int(input("Enter a number"))
# def check_if_even_or_odd():
#     if num%2 == 0:
#         print(f"{num} is even number")
#     else:
#         print(f"{num} is odd number")
# check_if_even_or_odd()

#program to define a function which can print a dictionary where the keys are numbers between 1 and 20 
# (both included) and the values are square of keys.
# def print_square_of_keys():
#     dict_num = {num: num**2 for num in range(1,21)}
#     print(dict_num)
# print_square_of_keys()

# Write a program to take a string as input and return a string with vowels removed.
# (implement List Comprehesion)
# def remove_vowels_from_string():
#     str1 = input("Enter a string: ")
#     list1 = [n for n in str1 if n not in "aeiou"]
#     str2 = ' '.join(list1)
#     print(str2)

# remove_vowels_from_string()

#program to display Powers of 2 using Anonymous functions?(lambda,map).
# num_list = [num for num in range(1,11)]
# powers_of_2 = list(map(lambda x:x**2, num_list))
# print(powers_of_2)

#program to take two list of same length as input and return a dictionary with one as keys and other as values.
# def create_dict():
#     keys = input('Enter numbers seperated by comma').split(',')
#     values = input('Enter numbers seperated by comma').split(',')
#     result = {}
#     for i in range(len(keys)):
#         result[keys[i].strip()] = values[i].strip()
#     print(result)

    # dict_n = {key: value for key, value in zip(list_1, list_2)}   # Using zip method
    # print(dict_n)
        
# create_dict()

# #program to print fibonocci series
# def print_fibonocci_series(n):
#     a,b=0,1
    
#     for i in range(n):
#         print(a,end=' ')
#         a,b=b,a+b

# n = int(input('Enter the limit: '))
# print_fibonocci_series(n)
    

# program to print factorial of a number using recursion.
# def print_factorial():
#     num = int(input('Enter a number: '))
#     f=1
#     for i in range(1,num+1):
#         f=f*i
#     print(f'Factorial of {num} = {f}')

# print_factorial()





