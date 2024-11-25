"""
returns the result of an arithmetic operation
"""

INPUT = (2, 3, "+")
# INPUT = (2,3, "%")
# INPUT = (2,3, "**")
# INPUT = (2,3, "*")
# INPUT = (2,3, "-")


def calculate(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '%':
        return number1 % number2
    elif operator == '**':
        return number1 ** number2
    else:
        return "Invalid operator"


def main():
    print(f'{calculate(*INPUT)}')


if __name__ == '__main__':
    main()
