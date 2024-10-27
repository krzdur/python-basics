"""
Checks whether the vehicle speed entered from the keyboard is correct.
"""

speed_str = input("Enter vehicle speed: ")
speed = int(speed_str)
is_valid = speed >=40 and speed <= 140

print(f"Speed is valid: {is_valid}")
