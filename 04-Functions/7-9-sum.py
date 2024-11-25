# INPUT = (3124, True)
# INPUT = (3124, False)
# INPUT = (20576, False)
# INPUT = (20576, True)
INPUT = (13115, True)


def sum_numbers(number, even):
    number_str = str(number)
    return sum(int(digit) for digit in number_str if _is_even(int(digit)) == even)


def _is_even(digit):
    return digit % 2 == 0


def main():
    print(sum_numbers(*INPUT))
    

if __name__ == '__main__':
    main()
