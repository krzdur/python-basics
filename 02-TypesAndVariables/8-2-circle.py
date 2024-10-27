###
# Calculation of circle area and circumference
#
import math

# determine radius and PI values
r = int(input("Provide radius: "))
pi = math.pi

# calculate area
a = pi * r**2

# calculate circumference
c = 2 * pi * r

# print results
print(f"""
Area: {round(a, 2)}
Circumferece: {round(c, 2)}
""")
