"""
returns True if at least one of the numbers n1,n2,n3 is negative or False otherwise
"""

INPUT = (11,6,-4)
# INPUT = (5,4,14)


def one_is_negative(n1, n2, n3):
    return n1 < 0 or n2 < 0 or n3 < 0


def main():
    print(f'{one_is_negative(*INPUT)}')
    

if __name__ == '__main__':
    main()
