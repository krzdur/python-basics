"""
Calculates the amount to be paid. Read the number of purchased products and the product price from the keyboard.
A 25% discount is charged for each product purchased over two.

Sample result:
Number of products purchased: 5
Product price: 40
Amount to pay: 170.00
"""

product_cnt = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

if product_cnt > 2:
    total = 2 * product_price + (product_cnt -2) * product_price * 0.75
else:
    total = product_cnt * product_price

print(f"Amount to pay: {total}")