# The Greatest Showdown
# Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. 
# Your code should then identify and print out the largest number among the three.

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

largest = max(num1, num2, num3)

# Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number 
# among the three and print it out.

smallest = min(num1, num2, num3)

# Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. 
# The largest number is 4. "

print(f"The smallest number is {smallest}. The largest number is {largest}.")
