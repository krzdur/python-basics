# INPUT_VALUE = 23
# INPUT_VALUE = 8
# INPUT_VALUE = 2
INPUT_VALUE = 0


def count_coins(amount_to_pay):
    reminder = amount_to_pay

    coins_5 = reminder // 5
    reminder = reminder % 5

    coins_2 = reminder // 2
    reminder = reminder % 2

    coins_1 = reminder

    return sum((coins_5, coins_2, coins_1))


def main():
    print(count_coins(INPUT_VALUE))
    

if __name__ == '__main__':
    main()
