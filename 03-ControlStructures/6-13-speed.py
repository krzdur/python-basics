"""
The speed of vehicles on highways in Poland is at least 40 km/h and not more than 140 km/h.
The program that prints a message when the specified car speed, read from the keyboard, has been exceeded.

Sample result:
Enter car speed: 38
Warning: invalid car speed!!
"""
speed_limit_min = 40
speed_limit_max = 140

car_speed = float(input("Enter car speed: "))

if speed_limit_min > car_speed or car_speed > speed_limit_max:
    print("Warning: invalid car speed!!")
