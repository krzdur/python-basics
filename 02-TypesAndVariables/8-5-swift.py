###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input('Provide a SWIFT code: ')

bank_code = swift[:4]
country_code = swift[4:6]

print(f'Bank Code: {bank_code}')
print(f'Country Code: {country_code}')