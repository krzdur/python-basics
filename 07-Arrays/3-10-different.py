arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]


def main():
    result = [num for num in arr1 if num not in arr2]
    print(result)
    

if __name__ == '__main__':
    main()
