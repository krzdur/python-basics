"""
Asks for the number of hours of parking, then calculates and prints the correct fee
1-2 hours: 5 PLN
3-6 hours: 15 PLN
Over 6 hours: 20 PLN
"""
hours = int(input("Provide the number of parking hours: "))

if hours > 6:
    print(f"The fee is 20 PLN")
elif hours >= 3:
    print(f"The fee is 15 PLN")
elif hours >= 1:
    print(f"The fee is 5 PLN")
else:
    print("The number of hours must be greater than 0")