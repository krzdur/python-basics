"""
returns a sentence with spaces removed
"""

INPUT = "integrated development environment"


def remove_spaces(sentence):
    return sentence.replace(" ", "")


def main():
    print(f'{remove_spaces(INPUT)}')
    

if __name__ == '__main__':
    main()
