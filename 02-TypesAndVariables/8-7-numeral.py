"""
Reads an integer number from the keyboard and prints that value as a binary and hexadecimal number.
"""

x = int(input("Enter number: "))

x_bin = bin(x)
x_hex = hex(x)

print(f"""
Binary number: {x_bin}
Hexadecimal number: {x_hex}
""")
