"""
returns the sum of repeated digits in a number
"""
# INPUT = 1027
INPUT = 230335
# INPUT = 513553007


def sum_repeated(number):
    num_str = str(number)

    digit_counts = {}
    for digit in num_str:
        digit_counts[digit] = digit_counts.get(digit, 0) + 1

    repeated_sum = sum(int(digit) * count for digit, count in digit_counts.items() if count > 1)

    return repeated_sum


def main():
    print(f'{sum_repeated(INPUT)}')


if __name__ == '__main__':
    main()
