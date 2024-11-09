"""Asks the user for their age and then checks which age group they belong to:

Child: under 13
Teen: 13 to 19
Adult: 20 to 64
Senior: 65 or older"""

age = int(input("Provide you age: "))

if age >= 65:
    print("You're a Senior")
elif age >= 20:
    print("You're an Adult")
elif age >= 13:
    print("You're a Teen")
elif age < 13:
    print("You're a Child")
else:
    print("The age must be greater than 0")
