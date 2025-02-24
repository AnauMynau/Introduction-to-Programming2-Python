'''Task 1. Calculate Your Final Trimester GPA!'''


# Function for converting percentages to GPA points
def calculate_gpa(grades):
    
    courses = [
        "Introduction to Programming II",
        "Object-Oriented Programming",
        "Discrete Mathematics",
        "Calculus II",
        "Political Science",
        "Foreign Language 1",
        "Foreign Language 2",
    ]
    
    if len(grades) != 7:
        return "Error: You must provide grades for all 7 courses"

    for grade in grades:
        if not isinstance(grade, (int, float)):
            return f"Error: {grade} is not a valid number"
        
        
        if grade < 0 or grade > 100:
            return f"Error: {grade} is not between 0 and 100"

    total_points = 0
    credits = 5
    total_credits = 7 * credits

    grading_scale = [
        (95, 100, 4.0),
        (90, 94, 3.67),
        (85, 89, 3.33),
        (80, 84, 3.0),
        (75, 79, 2.67),
        (70, 74, 2.33),
        (65, 69, 2.0),
        (60, 64, 1.67),
        (55, 59, 1.33),
        (50, 54, 1.0),
        (0, 49, 0.0),
    ]

    for grade in grades:
        for min, max, gpa in grading_scale:
            if min <= grade <= max:
                total_points += gpa * credits
                break


    gpa = round(total_points / total_credits, 2)
    return gpa




''' Task 2. Class GPA Calculator 📊'''

def calculate_class_gpa(class_data):
    total_gpa = 0
    student_count = len(class_data)

    for student, grades in class_data.items():
        gpa = calculate_gpa(grades)
        total_gpa += gpa

    avg_gpa = total_gpa / student_count
    return round(avg_gpa, 2)




'''Task 3. Password Validator Function'''

def is_valid_password(password):
    
    uppercase_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lowercase_chars = set('abcdefghijklmnopqrstuvwxyz')
    numbers = set('0123456789')
    special_chars = set('!@?')
    
    if len(password) < 8:
        return False
    
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    
    
    for char in password:
        if char in uppercase_chars:
            has_uppercase = True
        elif char in lowercase_chars:
            has_lowercase = True
        elif char in numbers:
            has_digit = True
        elif char in special_chars:
            has_special_char = True
            
        if has_uppercase and has_lowercase and has_digit and has_special_char:
            return True
        
    return False


# while True:
    
#     password = input("Enter a password: ")
    
#     if is_valid_password(password):
#         print("Password is valid") #Noyan1!@? 
#         break
#     else:
#         print("Password is invalid.\n Please enter a password that is at least 8 characters with: !, @, ?")
        
        
        
        
'''Task 4.Rock Paper Scissors Lizard Spock 🎮'''

import random

def play_rpsls(user_choice):
    
    choises = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    
    user_choice = user_choice.lower()
    if user_choice not in choises:
        print("Invalid choice!")
        print("Valid choices are: Rock, Paper, Scissors, Lizard, Spock.")
        return

    computer_choice = random.choice(choises)
    
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or \
         (user_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or \
         (user_choice == "rock" and (computer_choice == "lizard" or computer_choice == "scissors")) or \
         (user_choice == "lizard" and (computer_choice == "spock" or computer_choice == "paper")) or \
         (user_choice == "spock" and (computer_choice == "scissors" or computer_choice == "rock")):
        result = "You win!"
    else:
        result = "You lose!"

 
    print(f"You chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    print(f"Result: {result}")

    
    
    
'''Task 5. Age Calculator 📅'''

def calculate_age(birth_date_str):
    
    from datetime import datetime
    
   
    months = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4,
        'may': 5, 'june': 6, 'july': 7, 'august': 8,
        'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    

    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }

    
    current_year = 2024
    current_month = 1
    current_day = 6


    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    
    if is_leap_year(current_year):
        days_in_month[2] = 29

    
    parts = birth_date_str.lower().split()
    if len(parts[0]) == 4:  # format: YYYY Month DD
        birth_year = int(parts[0])
        birth_month = months[parts[1]]
        birth_day = int(parts[2])
    else:  # format: DD Month YYYY
        birth_day = int(parts[0])
        birth_month = months[parts[1]]
        birth_year = int(parts[2])

    years = current_year - birth_year
    months = current_month - birth_month
    days = current_day - birth_day

    if days < 0:
        previous_month = current_month - 1 if current_month > 1 else 12
        days += days_in_month[previous_month]
        months -= 1

    if months < 0:
        months += 12
        years -= 1


    return f"You are {years} years, {months} months, and {days} days old."