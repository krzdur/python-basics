"""
Allows you to enter the product price and discount. Print the product price, discount, discounted product price, and the
difference between the product price before and after the discount
"""

price_str = input("Enter the original price: ")
discount_str = input("Enter the discount (in %): ")

price = float(price_str)
discount = int(discount_str)

price_w_discount = price - price * discount/100
reduction = price_w_discount - price

print(f"""
Entered price: {round(price, 2)}
Entered discount %: {discount}
Price with discount: {round(price_w_discount)}
Reduction: {round(reduction, 2)}
""")