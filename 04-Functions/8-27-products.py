"""
Returns True if the product code is correct or False otherwise.
Products are marked with a special code consisting of 3 digits and a fourth control digit. The forth digit is determined
by calculating the remainder of dividing the sum of the first three digits by 7.
"""
# INPUT = "1082"
# INPUT = "2035"
# INPUT = "1114"
INPUT = "7071"


def validate(product_code):
    digits = [int(digit) for digit in product_code]

    if len(digits) != 4:
        return False

    sum_first_three = sum(digits[:3])
    control_digit = sum_first_three % 7
    return control_digit == digits[3]


def main():
    print(f"Code valid: {validate(INPUT)}")


if __name__ == '__main__':
    main()
