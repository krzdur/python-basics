"""
Returns the given text with all characters separated by a dash sign
"""

INPUT = "Univesity"
# INPUT = "UE"
# INPUT = "x"
# INPUT = ""


def join_w_dashes(text):
    return '-'.join(text)


def main():
    print(f'{join_w_dashes(INPUT)}')


if __name__ == '__main__':
    main()
