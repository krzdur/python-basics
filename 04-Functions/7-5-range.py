from helpers import in_range


def main():
    value = int(input('A number: '))
    range_start = int(input('Range start: '))
    range_end = int(input('Range end: '))

    print(f'Number {value} in the range <{range_start},{range_end}>: {in_range((range_start, range_end), value)}')


if __name__ == '__main__':
    main()
