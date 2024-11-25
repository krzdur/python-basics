"""
returns the difference between the largest and smallest numbers
"""
INPUT = (7, 4, 9)
# INPUT = (2, 12, 8)


def largest_smallest_diff(number1, number2, number3):
    largest = max(number1, number2, number3)
    smallest = min(number1, number2, number3)
    return largest - smallest


def main():
    print("Difference:", largest_smallest_diff(*INPUT))


if __name__ == '__main__':
    main()
