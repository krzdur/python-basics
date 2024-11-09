###
# Calculates the number of days in a month
#
month = int(input('Enter month number (1..12): '))

months_31 = (1, 3, 5, 7, 8, 10, 12)

if month > 12:
    raise ValueError("Month must be between 1 and 12")
elif month in months_31:
    days = 31  # months with 31 days
elif month not in months_31 and month != 2:
    days = 30
elif month == 2:  # February 28 days
    days = 28

print(f'Month {month} has {days} days')
