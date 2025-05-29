# 🧮 Binary to Decimal Converter

# Function to convert binary to decimal
def binary_to_decimal(binary_str):
    """
    Converts a binary string (e.g., '1010') to its decimal equivalent.
    """
    try:
        # Use Python's built-in int() function with base 2
        decimal_value = int(binary_str, 2)
        return decimal_value
    except ValueError:
        # Handle the case where input is not a valid binary number
        return "Invalid binary number. Please enter only 0s and 1s."

# Main program starts here
if __name__ == "__main__":
    # Ask user to enter a binary number
    binary_input = input("Enter a binary number (e.g., 1011): ")

    # Call the conversion function
    result = binary_to_decimal(binary_input)

    # Print the result
    print("Decimal value:", result)
