"""
For the given natural number n calculates the sum of all natural numbers between 1 and n.
"""
N = 10


def sum_natural(n):
    if n < 0:
        raise ValueError('`n` has to be a natural number (>=0)')
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    return n + sum_natural(n - 1)


def main():
    print(sum_natural(N))
    

if __name__ == '__main__':
    main()
