"""
make changes in your program code. Replace the 'for' with a 'while' statement.
7 8 9
4 5 6
1 2 3
"""

# for i in range(6,-1,-3):
#     for j in range(1,4):
#         print(f'{i+j}',end=' ')
#     print()


starting_num = 7

while starting_num > 0:
    row_num = 0
    while row_num < 3:
        print(starting_num + row_num, end=' ')
        row_num += 1
    print()
    starting_num -= 3
