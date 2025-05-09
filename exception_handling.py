# try:
#     result = 1 / 0
#     print(result)
    # arr = [5,7,4]
    # print(arr[3])

# except (ZeroDivisionError,IndexError):                  # Another form of declaring chained exception
    # print("Division by zero error or Index Error")

# except ZeroDivisionError:
#     print("Division by zero error")

# except IndexError:
#     print("Array index out of bounds error")

# except Exception:                                    # General exception
#     print("Exception occured. Please input valid data")

# else:
#     print("Exception was not occured")

# finally:
#     print("After try except block")

# Example:
# try:
#     num = int("welcome")
#     if num%2 == 0:
#         print(f"{num} is even number")
#     else:
#         print(f"{num} is odd number")

# except ValueError:
#     print("Please input valid data")

# try:
#     num_list = [4,2,6,7]
#     print(num_list.index(3))

# except ValueError:
#     print("Invalid data error")
    

# try:
#     import mathh
#     area = mathh.pi*5
#     print(area)

# except ImportError:
#     print("Import Error")

# try:
#     print(x)
# except NameError:
#     print("Name error..")

def check_prime(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
try:
    num = int(input("Enter a number: "))
    check_prime(num)

except ValueError:
    print("Invalid number")
