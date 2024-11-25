###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input("Provide letter and press enter: ")
print(f'Letter read from the keyboard: {letter}')

string = '20303'
print(f"Number representing the string \"20303\": {int(string)}")

bin_number = bin(304)
print(f'Binary string representing decimal number 304: {bin_number}')

hex_number = hex(304)
print(f'Hexadecimal string representing decimal number 304: {hex_number}')

int_euro = ord("€")
print(f'Integer representing the Unicode code of the € sign: {int_euro}')

abs_17 = abs(-17)
print(f'Absolute value of -17: {abs_17}')