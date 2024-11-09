"""
Converts a decimal number into a binary number. To convert a decimal number to binary, follow these steps:

Read a decimal number from the keyboard.
Divide the number by 2 and note the remainder.
Divide the quotient obtained by 2 and note the remainder.
Repeat the same process till we get 0 as the quotient.
Write the values of all the remainders starting from the bottom to the top. That will be the required binary number.
Sample result:

Enter decimal number: 12
12(10) = 1100(2)
"""

decimal = int(input("Enter decimal number: "))

binary = ""
quotient = decimal

while quotient != 0:
    reminder = quotient % 2
    binary = str(reminder) + binary
    quotient = quotient // 2

print(f"{decimal}(10) = {binary}(2)")

