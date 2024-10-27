"""
Prints the number of dice rolled and the value True if the number rolled is 1 or 6
"""
import random

rolled = random.randint(1, 6)
is_special = rolled in [1, 6]

print(f"""
Dice rolled: {rolled}
Special number (1 or 6): {is_special}
""")
