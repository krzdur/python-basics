"""
Checks whether the EAN-13 number entered from the keyboard consists of exactly 13 characters (digits).
Print a message if the number is correct. Additionally, only when the article number is correct, print a message
when the product was manufactured in Poland.

Sample result:
Enter EAN-13 article number: 5901230094938
Article number is correct
Article manufactured in Poland
"""

ean = input("Enter EAN-13 article number: ")

if not (ean.isdigit() or len(ean) == 13):
    print("EAN has to consist of 13 digits")
else:
    print("Article number is correct")
    if ean[:3] == '590':
        print("Article manufactured in Poland")





