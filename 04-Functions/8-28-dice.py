"""
Returns a number specifying the number of dice rolled the most times in a row.
The sequence of digits contains the number of points rolled with a dice.
"""
INPUT = "5233165554211"
# INPUT = "2133"


def most_frequent_result(dice):
    dice = [int(digit) for digit in dice]
    return max(set(dice), key=dice.count)


def main():
    print(f'Most frequent result: {most_frequent_result(INPUT)}')
    

if __name__ == '__main__':
    main()
