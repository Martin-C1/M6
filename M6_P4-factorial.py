#Martin Cahue
# October 31, 2024

import math
factorial_input = int(input("enter a factorial: "))
#the user enters a factorial
factorial_math = math.factorial(factorial_input)
#calculates the factorial for the user's number using the math module function math.factorial
factorial_result = 1
for i in range(1, factorial_input +1):
    factorial_result *= i
#calculates the factorial for the user's number using a for statement
print(f"The factorial of {factorial_input} using the math.factorial function is {factorial_math}")
print(f"The factorial of {factorial_input} using the for statement is {factorial_result}")
#prints the result of the factorial using both methods
if factorial_math == factorial_result:
    print("The results are the same using both methods")
else:
    print("The results are different")
#compares the results to determine if they are the same or different and prints the corresponding message

#P4- a program that calculates the factorial of a user input value