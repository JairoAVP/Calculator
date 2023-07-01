"""Assignment for Python - Calculator (part 1)

Purpose: To get familiar with functions.

Requirement: Please write a program and name it as Calculator. This program will let the user to enter two numbers and then return the sum. For example, the user enters 4 and 7, the program should return 11.

Score Breakdown:

- File naming (1 point)
- Main functionalities (3 points)
- Code quality (1 point)

Estimated hour: 0.5 hour

Key Words: function/method, variables, arguments"""




def sum(a, b):
    return a + b


number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

result = sum(number1, number2)

print(result)