"""
Determines in which quadrant of the coordinate system the point P(x, y) is located or on which axis it is located,
or that it is located in the position (0,0) of the coordinate system. Sample result:
"""

print("Provide the coordinates:")

x = int(input("x = "))
y = int(input("y = "))


if x == 0 and y == 0:
    print(f"Point P({x},{y}) is in the center of the coordinate system")
elif x == 0 and y != 0:
    print(f"Point P({x},{y}) lies on the y-axis of the coordinate system")
elif x != 0 and y == 0:
    print(f"Point P({x},{y}) lies on the x-axis of the coordinate system")
else:
    quadrant = str()
    if x > 0 < y:
        quadrant = 'first'
    elif x < 0 < y:
        quadrant = 'second'
    elif x < 0 > y:
        quadrant = 'third'
    elif x < 0 > y:
        quadrant = 'fourth'

    print(f"Point P({x},{y}) is in the {quadrant} quadrant of the coordinate system")