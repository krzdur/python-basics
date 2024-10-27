"""
Calculates the distance to the horizon from a height given in meters from the keyboard
"""
import math

# example
H_ON_THE_BEACH = 178
H_IN_THE_HOTEL = 20 * 100


# formula
def get_distance_to_horizon(h):
    h_in_m = h / 100
    return 3.57 * math.sqrt(h_in_m)


d = get_distance_to_horizon(H_ON_THE_BEACH)
print(f"Distance to horizon for my height: {d}")

d = get_distance_to_horizon(H_IN_THE_HOTEL)
print(f"Distance to horizon in the hotel: {d}")

# input
h = input("\nWhat is your height above the ground (in cm): ")
d = get_distance_to_horizon(int(h))

# output
print(f"Distance to horizon for the input: {d}")