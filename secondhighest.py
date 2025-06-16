if __name__ == '__main__':
    # Read the number of elements (not used directly here, but usually given in constraints)
    n = int(input())

    # Read the list of integers, convert to int, remove duplicates using set, and sort the result
    arr = sorted(set(map(int, input().split())))

    # Print the second largest unique element (second last in sorted list)
    print(arr[-2])
