"""
Based on the circumference of the tree entered from the keyboard, calculates and prints the value True if the tree
can be cut down, or print the value False otherwise
"""
import math

def can_cut_down(c):
    d = c / math.pi
    return d >= 50

c_str = input("Enter tree circumference in cm: ")
c = int(c_str)

print(f"Tree can be cut down: {can_cut_down(c)}")

trees_in_garden = {
    'Tree 1': 160,
    'Tree 2': 90,
    'Tree 3': 230,
    'Tree 4': 120
}

print('\nTrees in the garden:')
for t, c in trees_in_garden.items():
    print(f"{t} can be cut down: {can_cut_down(c)}")
