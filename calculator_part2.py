"""Assignment for Python - Calculator (part 2)

Purpose: To learn error handling.

Requirement: Please creat a new file and name it as calculator_part2.py. Copy all your code from calculator_part1.py to this new file.
This requirement is to handle the error. If the user enters a or b or whatever that is not a number, your current code will break. 
Please handle this error so that the user won’t see those error message that could frustrate them.

Estimated Hour: 0.5 hour"""




def calculator():
    while True:
        try:
            number1 = float(input("Please enter the first number: "))
            number2 = float(input("Please enter the second number: "))
            operation = input("Please enter an operator (+, -, *,/): ")


            if operation == "+":
                answer = number1 + number2
                print(f"{number1} + {number2} = {answer}")    
            elif operation == "-":
                answer = number1 - number2
                print(f"{number1} - {number2} = {answer}")     
            elif operation == "*":
                answer = number1 * number2
                print(f"{number1} * {number2} = {answer}")    
            elif operation == "/":
                answer = number1 / number2
                print(f"{number1} / {number2} = {answer}") 
            else:
                print("Invalid Operation entered. Please try again.")
                return
            
            print("Result:", answer)
        except ValueError:
                print("Invalid input. Please enter a valid number.")
        except ZeroDivisionError:
                print("Division by zero is not allowed")
            
            
calculator()