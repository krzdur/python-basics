"""
returns a string of n asterisks, separated by a slash sign
"""

N = 4


def get_asterisks(n):
    return '/'.join(['*'] * n)


def main():
    print(f'{get_asterisks(N)}')
    

if __name__ == '__main__':
    main()
