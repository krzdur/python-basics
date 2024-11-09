"""
There are coins of 1, 2 and 5 Polish Zlotys (PLN). Write a program showing any amount (natural number) read from the
keyboard with as few coins as possible.

Enter the amount in PLN: 18
The amount of PLN 18 in coins:
5 PLN coins: 3
2 PLN coins: 1
1 PLN coins: 1
"""

amount = int(input("Enter the amount in PLN: "))

reminder = amount

coins_5 = reminder // 5
reminder = reminder % 5

coins_2 = reminder // 2
reminder = reminder % 2

coins_1 = reminder

print(f"""
The amount of PLN {amount} in coins:
5 PLN coins: {coins_5}
2 PLN coins: {coins_2}
1 PLN coins: {coins_1}
""")