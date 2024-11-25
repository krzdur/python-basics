"""
returns the n-th prime number. A prime number is a natural number greater than 1, divisible by 1 and that number
"""
N = 5


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_nth_prime(n):
    primes_found = 0
    current_checked = 1

    while primes_found < n:
        current_checked += 1
        if is_prime(current_checked):
            primes_found += 1

    return current_checked


def main():
    print(f'{get_nth_prime(N)}')


if __name__ == '__main__':
    main()
