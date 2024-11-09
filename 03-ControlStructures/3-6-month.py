###
# Checks if the given day number of the month is correct
#
month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))
day_ok = False

months_31 = (1, 3, 5, 7, 8, 10, 12)

if month > 12:
    raise ValueError("Month must be between 1 and 12")
elif month in months_31:
    if day >=1 and day <= 31:
        day_ok = True
elif month not in months_31 and month != 2:
    if day >= 1 and day <= 30:
        day_ok = True
elif month == 2:  # February 28 days
    if day >= 1 and day <= 28:
        day_ok = True

message = f'Day {day} for the month {month}'
if day_ok:
    print(f'{message} is correct')
else:
    print(f'{message} is incorrect')