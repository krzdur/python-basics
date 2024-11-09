"""
Creates the following pattern:

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

num_stars = 5

for i in range(1, num_stars+1):
    print('* ' * i)

for i in reversed(range(1, num_stars)):
    print('* ' * i)
