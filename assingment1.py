#                                         Input and Prints 
# TASK 1


name = input("Enter your name: ")
language = input("Enter your favorite programming language: ")

print(f"Hello, {name}! You love {language}")

#############################################################################################################
# TASK 2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum_of_numbers = num1 + num2
difference_of_numbers = num1 - num2

print(f"The sum of {num1} and {num2} is {sum_of_numbers}")
print(f"The difference between {num1} and {num2} is {difference_of_numbers}.")

#############################################################################################################

#                                     Numbers and Arithmetic Operations 
# TASK 3

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

area = length * width

print(f"The area of the rectangle is {area}")

#############################################################################################################

# TASK 4

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by 3 and 5.")
else:
    print(f"{number} is not divisible by 3 and 5.")


#############################################################################################################

#                                            Strings and Lists 
# TASK 5

sentence = input("Enter a sentence: ")
word_count = len(sentence)
uppercase_sentence = sentence.upper()
sentence = sentence.split()

print(f"The sentence in uppercase: {uppercase_sentence}")
print(f"Number of words: {word_count}")


#############################################################################################################

# TASK 6

fruit1 = input("Enter your favorite fruit 1: ")
fruit2 = input("Enter your favorite fruit 2: ")
fruit3 = input("Enter your favorite fruit 3: ")
fruit4 = input("Enter your favorite fruit 4: ")
fruit5 = input("Enter your favorite fruit 5: ")

print(f"Your favorite fruits in reverse order: {fruit5}, {fruit4}, {fruit3}, {fruit2}, {fruit1}")

#############################################################################################################

#                                     Conditionals 

# TASK 7

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#############################################################################################################


# TASK 8

# number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#############################################################################################################


#                                                   Loops 
# TASK 9

number = int(input("Enter a number: "))

print(f'Even numbers from 1 to {number}: ', end="")
for i in range(1, number + 1):
    if i % 2 == 0:
        print(i, end=" ")

#############################################################################################################


#  TASK 10

number = int(input("Enter a number: "))
factorial = 1
print(f"The factorial of {number} is", end=" ")
for i in range(1, number + 1):
    factorial *= i

print(factorial, end=" ")
    

#############################################################################################################
