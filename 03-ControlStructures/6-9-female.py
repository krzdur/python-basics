"""Prints the name entered from the keyboard, provided it is a female name. Sample result:

Enter name: Anna
Anna -- Polish female name"""

name = input("Provide a name: ")

if name[-1] == 'a':
    print(f'{name} -- Polish female name')
else:
    print(f'{name} -- Polish male name')