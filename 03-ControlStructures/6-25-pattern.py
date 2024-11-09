"""
Creates the following pattern:

1
22
333
4444
55555
666666
7777777
88888888
999999999
"""

num_lines = 9

for i in range(1, num_lines+1):
    print(f'{i}'*i)