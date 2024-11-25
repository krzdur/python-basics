# INPUT_NUM = '101101'
INPUT_NUM = '1311a10100'


def is_binary(number: str) -> bool:
    return all([(num == '1') or (num == '0') for num in number])


def main():
    print(is_binary(INPUT_NUM))
    

if __name__ == '__main__':
    main()
