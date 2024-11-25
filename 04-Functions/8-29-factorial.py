"""
Calculate the factorial value for n = 5
"""
N = 5


def factorial(n):
    # 0! = 1, 1! = 1
    if n == 0 or n == 1:
        return 1

    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n - 1)


def main():
    print(f'{factorial(N)}')


if __name__ == '__main__':
    main()
