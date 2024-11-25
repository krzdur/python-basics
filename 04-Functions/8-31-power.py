"""
Calculates x^n
"""
BASE = 5
EXPONENT = 3


def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * power(base, exponent-1)
    else:
        return 1 / power(base, -exponent)


def main():
    print(f'{BASE} to the power of {EXPONENT} = {power(BASE, EXPONENT)}')
    

if __name__ == '__main__':
    main()
