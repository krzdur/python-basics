from helpers import count_letters


SENTENCE = 'You never get a second chance to make a first impression'
LETTER = 'e'


def main():
    print(f'The number of letter \'{LETTER}\': {count_letters(SENTENCE, LETTER)}')


if __name__ == '__main__':
    main()
