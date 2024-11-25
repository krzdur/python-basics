def month(month_num):
    if month_num > 12:
        raise ValueError('Month number can\'t be greater than 12')

    month_dict = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    print(f'The name of month {month_num} is {month_dict[month_num]}')


def count_letters(string: str, letter: str) -> int:
    if len(letter) > 1:
        raise ValueError('You can provide 1 letter only.')
    return string.count(letter)


def in_range(from_to: tuple, value: int) -> str:
    is_in_range = from_to[0] <= value <= from_to[1]
    if is_in_range:
        return 'yes'
    else:
        return 'no'


def hide(card_number):
    if len(card_number) != 16:
        raise ValueError('This is not a valid credit card number!')
    return f'{card_number[:2]}{"*"*10}{card_number[-4:]}'

