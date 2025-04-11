# Count characters in a string
# text = "hello"
# result = {}

# for i in text:
#     if i in result:
#         result[i] = result[i] + 1   # Increment value of the corresponding key value 
#     else:
#         result[i] = 1

# print(result)

# Count vowels in a string
# text = "hello"
# result = {}

# for i in text:
#     if i in result:
#         if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
#             result[i] = result[i] + 1   # Increment value of the corresponding key value 
#     else:
#         result[i] = 1

# print(result)

# Count words in a text
# text = "Welcome to Ooty. Welcome All"
# words = text.split()
# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word]+=1
#     else:
#         word_count[word]=1
# else:
#     print("Exited")

# print(word_count)

#Find duplicate characters in a string
# text = "programming"
# duplicates = []
# for c in text:
#     if text.count(c) > 1 and c not in duplicates:
#         duplicates.append(c)
# print(duplicates)

#Reverse a string
# str = "Good Morning"
# print(str[::-1])

#Print pattern
# n=int(input("Enter the range: "))
# i=1
# while i<=n:
#     print("*" * i)
#     i+=1

#Sum of a list of numbers
# n=int(input("Enter the range: "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# else:
#     print("Exit For loop")
# print("Sum= ",sum)

#Multiplication table
# n=int(input("Enter number"))
# for i in range(1,11):
#    print(f"{n} * {i} = {n * i}")

#Reverse a number
# num = int(input("Enter number"))
# rev = 0
# while(num > 0):
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# print(f"Reversed number= {rev}")
#  === OR ===
# num = int(input("Enter number"))
# sign=-1 if num < 0 else 1 # For negative number
# num = abs(num)
# n = int(str(num)[::-1]) * sign
# print(n)

# f=1
# for num in range(1,6):
#  f=f*num
# print(f)
# OR
# import math
# print(math.factorial(5))