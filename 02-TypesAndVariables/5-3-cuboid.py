###
# A program that calculates the volume
# and surface area of a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a_str = input('a=')
b_str = input('b=')
c_str = input('c=')

a = int(a_str)
b = int(b_str)
c = int(c_str)

volume = a * b * c
surface = 2 * a * b + 2 * b * c + 2 * a * c

print(f'The volume of a cuboid is {volume}')
print(f'The surface area of a is {surface}')
