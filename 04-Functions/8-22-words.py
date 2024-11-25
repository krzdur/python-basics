"""
returns the acronym (first letters of all words)
"""

INPUT = "Internet of Things"
# INPUT = "For Your Information"
# INPUT = "Python"


def get_acronym(name):
    acronym = ''.join(word[0] for word in name.split() if word)
    return acronym


def main():
    print(f"Acronym: {get_acronym(INPUT)}")


if __name__ == '__main__':
    main()
