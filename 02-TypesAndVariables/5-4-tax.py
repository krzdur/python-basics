"""
Reads an amount from the keyboard. Then, it calculates and prints both the amount and its VAT.
"""

amount_str = input("Provide the amount: ")
amount = float(amount_str)

vat = amount * 0.23

print(f"""
Amount  : {round(amount, 2)}
VAT 23% :  {round(vat, 2)}
""")