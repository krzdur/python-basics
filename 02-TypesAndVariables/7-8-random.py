###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random
dice_roll_1 = random.randint(1,6)
dice_roll_2 = random.randint(1,6)
dice_roll_3 = random.randint(1,6)
...
total = dice_roll_1 + dice_roll_2 + dice_roll_3

print(f"""
Roll 1: {dice_roll_1}
Roll 2: {dice_roll_2}
Roll 3: {dice_roll_3}

Sum: {total}
""")