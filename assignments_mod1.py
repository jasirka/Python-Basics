# Program to reverse a given string
# str = "Python"
# print(str[::-1])

# Program to determine if a given year is leap year
# year = int(input("Enter an year: "))

# if(year%4 == 0 and year%100 !=0 or year%400 == 0):
#     print(f"{year} is a leap year")
# else:
#      print(f"{year} is  not a leap year")

# Program to calculate the area and perimeter of a rectangle
# length = int(input("Enter the length of the rectangle: "))
# width = int(input("Enter the width of the rectangle: "))

# area = length * width
# perimeter = 2 * (length + width)

# print(f"Area of the rectangle= {area}")
# print(f"Perimeter of the rectangle= {perimeter}")

# Program to check if a number is prime number or not
# num = int(input("Enter a number: "))

# flag = False
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             flag = True
#             break
#     if flag:
#         print(f"{num} is not a prime number")
#     else:
#         print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

#Program to display the multiplication table
# num = int(input("Enter a number"))
# for n in range(1, 11):
#     print(f"{num} * {n} = {num * n}")

#Program to find the sum of n natural numbers
# n = int(input("Enter the value for n: "))
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i
# print(f"Sum of {n} numbers= {sum}")

#Program to count the number of vowels in a given string
# str = input("Enter a string: ")
# count = 0
# for c in str:
#     if(c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
#         count+=1

# print(f"No of vowels= {count}")

#Program to find the Addition,Subtraction,Multiplication and division on Complex-No's.
# i1 = int(input("Enter the real part for the first complex no"))
# j1 = int(input("Enter the imaginary part for the first complex no"))
# a = complex(i1,j1)
# i2 = int(input("Enter the real part for the second complex no"))
# j2 = int(input("Enter the imaginary part for the second complex no"))
# b = complex(i2,j2)
# print(f"Result of the sum of the two complex numbers= {a + b}")
# print(f"Result of the substraction of the two complex numbers= {a - b}")
# print(f"Result of the multiplication of the two complex numbers= {a * b}")
# print(f"Result of the division of the two complex numbers= {a / b}")

#program to find the factorial of the given number
# num = int(input("Enter a number"))
# f = 1
# for i in range(1, num+1):
#     f = f * i
# print(f"Factorial of {num} = {f}")

#program to find the largest among 3 numbers.
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))

# if a > b and a > c:
#     print(f"{a} is greater")
# elif b > a and b > c:
#     print(f"{b} is greater")
# else:
#     print(f"{c} is greater")

# program to find sum of all integers greater than 100 and less than 200 that are divisible by 7.
# sum=0
# for n in range(101, 200):
#     if n % 7 == 0:
#         sum+=n
# print(f"Sum of all integers greater than 100 and less than 200 that are divisible by 7 = {sum}")

# Program to swap two variables.
# a = int(input("Enter value for a: "))
# b = int(input("Enter value for b: "))
# print("Before swapping")
# print("value of a=", a)
# print("value of b=", b)
# temp = a
# a = b
# b = temp
# print("After swapping")
# print("value of a=", a)
# print("value of b=", b)

#Program to display the data type of user input.
user_input = input("Enter some string data: ")
print(f"Data type of the entered data is {type(user_input)}")

user_input = int(input("Enter some integer data: "))
print(f"Data type of the entered data is {type(user_input)}")

#Program to check whether a string is a palindrome or not.
# text = input("Enter a string: ")
# reversed = text[::-1]
# if text == reversed:
#     print(f"{text} is palindrome")
# else:
#     print(f"{text} is not palindrome")

#program using range() to print numbers from 1 to 10
# for n in range(1, 11):
#     print(n)
