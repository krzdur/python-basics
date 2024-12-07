def read_pets(file='pets.txt'):
    with open(file, 'r') as f:
        content = f.read()

    print(content)

    words = content.split()
    print('\n Word count:', len(words))


def main():
    read_pets()


if __name__ == '__main__':
    main()
