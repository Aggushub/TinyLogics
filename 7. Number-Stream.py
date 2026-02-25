# Main entry point of the program
if __name__ == '__main__':
    # Read an integer input from the user
    n = int(input())
    
    # Print numbers from 1 to n without any spaces between them
    # The '*' unpacks the range into separate arguments
    # 'sep' defines what separates the values ('' = no space)
    print(*range(1, n + 1), sep='')
