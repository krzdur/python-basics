###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = float(input("Provide the first number: "))
number2 = float(input("Provide the second number: "))
operator = input("Provide the operator (+, -, *, /): ")

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2
else:
    raise ValueError('Operator must be one of (+, -, *, /)')

# print result
print(f'{number1} {operator} {number2} = {result}')