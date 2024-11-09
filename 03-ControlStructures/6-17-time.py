"""
Allows you to convert time in 24-hour format to 12-hour format. The time in 24-hour format (hh:mm) is read from the keyboard.

Sample result:
Enter time (24-hour format): 16:32
Time in 12-hour format: 4:32pm
"""

time_24 = input("Enter time (24-hour format): ")

time_24_hour, time_24_minute = time_24.split(':')

if int(time_24_hour) > 12:
    time_12_hour = int(time_24_hour) - 12
    am_pm = 'pm'
else:
    time_12_hour = time_24_hour
    am_pm = 'am'

print(f"Time in 12-hour format: {time_12_hour}:{time_24_minute}{am_pm}")

