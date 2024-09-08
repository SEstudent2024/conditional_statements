# Leap Year Explorer
# Task 1: Leap Year Checker Write a Python program that prompts the user to input a year. 
# The program should determine if the given year is a leap year or not and then display an appropriate message. 
# Please note that this is the definition of a leap year: Every year that is exactly divisible by four is a leap year, 
# except for years that are exactly divisible by 100, but these centurial years are leap years if they are 
# exactly divisible by 400.

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
try:
    year_input = int(input("Enter a year: "))
    if leap_year(year_input):
        print(f"{year_input} is a leap year.")
    else:
        print(f"{year_input} is not a leap year.")
except ValueError:
    print("Please enter a valid year.")

# Expected Outcome: If you test the year 1900, is should be False. 
# The year 2000 should be True. The year 2024 should be True

