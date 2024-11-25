###
# Functions to read any data type from the keyboard
#
def input_string(message):
    message_str = input(message)
    return message_str


def input_integer(message):
    message_str = input(message)
    return int(message_str)


def input_real(message):
    message_str = input(message)
    return float(message_str)


def input_boolean(message):
    message_str = input(message)
    if message_str == 'y':
        message_bool = 1
    elif message_str == 'n':
        message_bool = 0
    else:
        ValueError('Input must be `y` or `n`.')
    return bool(message_bool)