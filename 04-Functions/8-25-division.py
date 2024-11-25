"""
Returns the sum of numbers in the range <x,y> that are completely divisible by 2 and 3 and not divisible by 4
"""
# INPUT = (1,20)
INPUT = (10,30)


def sum_of_divisible_23(x, y):
    total = 0

    for num in range(x, y + 1):
        if num % 2 == 0 and num % 3 == 0 and num % 4 != 0:
            total += num
    return total


def main():
    print(f'{sum_of_divisible_23(*INPUT)}')
    

if __name__ == '__main__':
    main()
