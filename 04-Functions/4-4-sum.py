###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number_abs = abs(number)
    number_str = str(number_abs)

    digit_sum = 0
    for l in number_str:
        digit_sum += int(l)

    return digit_sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')