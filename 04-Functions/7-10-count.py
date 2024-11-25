"""
returns the number of negative even numbers in the range <x,y>
"""
INPUT = (-7, 8)
# INPUT = (-1, 11)


def count_even_negative(x, y):
    # Count negative even numbers in range
    count = 0
    for num in range(x, y + 1):
        if num < 0 and num % 2 == 0:
            count += 1

    return count


def main():
    print(f'{count_even_negative(*INPUT)}')


if __name__ == '__main__':
    main()
