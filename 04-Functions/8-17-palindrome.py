"""
returns True if the expression is a palindrome or False otherwise
"""
# INPUT = "radar"
# INPUT = "12-11-21"
INPUT = "book"


def is_palindrome(expression):
    return expression == expression[::-1]


def main():
    print(f'{is_palindrome(INPUT)}')
    

if __name__ == '__main__':
    main()
