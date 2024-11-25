"""
Returns True if the password is correct or False otherwise.
A valid password should consist of at least six characters and each character appears only once in the password.
"""
# INPUT = "ax15"
# INPUT = "book123"
# INPUT = "A2water3"
# INPUT = "qwerty"
INPUT = ""


def validate_pass(password):
    return len(password) >= 6 and len(set(password)) == len(password)


def main():
    print(f"Correct password: {validate_pass(INPUT)}")


if __name__ == '__main__':
    main()
