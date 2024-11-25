"""
returns numbers from 1 to n as a string
"""
INPUT = 11


def get_numbers(n):
    result = ""
    for i in range(1, n + 1):
        result += str(i)
    return result


def main():
    print(f'{get_numbers(INPUT)}')


if __name__ == '__main__':
    main()
