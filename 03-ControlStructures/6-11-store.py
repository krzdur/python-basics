"""
Analyses the price of a product in an online store. If the product price decreases by at least 10%, the program prints
a purchase recommendation:

Buy the product!!
Product price reduced by 17%

The current and previous price of the product are included in variables.

Sample result:
Current product price: 140.00
Previous product price: 200.00
Buy the product!!
Product price reduced by 30%
"""

current_price = 140
previous_price = 200

price_change = current_price / previous_price - 1
price_change_int = abs(int(price_change * 100))

print(f"""
Current product price: {current_price}
Previous product price: {previous_price}""")

if price_change <= -0.1:
    print("Buy the product!!")
    print(f"Product price reduced by {price_change_int}%")
