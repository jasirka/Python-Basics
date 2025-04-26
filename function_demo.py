# Define function
# def sum(a,b):
#     sum = a+b
#     print(sum)

# sum(4,5)

# Default arguments
# def sum(a=2, b=1):
#     sum = a+b
#     print(sum)

# sum()

#Return values
# def sum_and_return(a,b):
#     sum = a + b
#     return sum

# print(sum_and_return(5,6))

#Arbitrary arguments
# def sum_arbitrary_args(*numbers):
#     result = 0
#     for num in numbers:
#         result = result + num
#     return result

# print(sum_arbitrary_args(4,6,7,2))

#Arbitrary keyword arguments
# def sum_arbitrary_keywrd_args(**fruits):
#     for i in fruits.items():
#         print(i)

# sum_arbitrary_keywrd_args(name="apple",price="$45",quantity="5kg")

s = lambda a,b: a+b  # Anonymous function
print(s(4,5))


