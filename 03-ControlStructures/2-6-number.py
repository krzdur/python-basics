"""Checks what number was entered from the keyboard and prints one of the messages below."""

num = int(input("Provide a number: "))

if num > 0:
    print(f"Number {num} is positive")
elif num < 0:
    print(f"Number {num} is negative")
else:
    print("Number is 0")