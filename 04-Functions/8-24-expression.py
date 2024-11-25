"""
Returns the value of the expression
An expression contains operators for adding and subtracting single-digit numbers.
"""
# INPUT = "2+3"
# INPUT = "3+8+1"
INPUT = "2+3-4+5-0"


def evaluate(expression):
    return eval(INPUT)


def main():
    print(f'Result: {evaluate(INPUT)}')


if __name__ == '__main__':
    main()
