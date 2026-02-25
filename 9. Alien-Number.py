"""
👾🌌 The Legend of the Alien Number 🌌👾

Long ago, in a distant star system called Primonia, aliens didn't use regular numbers.
Instead, their entire mathematical system was based on the mysterious power of **prime numbers**.
They believed primes were the building blocks of the universe — divine and indivisible.

To communicate across galaxies, they created a secret code: the **Alien Number**.

Here's how it works:

🪐 Step 1: Take two signals — integers 'a' and 'b'
🪐 Step 2: Decode them into their respective prime identities:
    - Find the 'a'th prime number
    - Find the 'b'th prime number
🪐 Step 3: Multiply or add these primes together — the result represents energy exchange.
🪐 Step 4: To complete the code, reduce the product by exactly 1 unit.
    - Why subtract 1? Because in Primonian lore, nothing is ever complete without a spark of mystery.

This final number is what we call the **Alien Number** —
a sacred numerical beacon sent from one mind to another, across the cosmic void.

Now you're about to compute it, Earthling.
"""

# This is the Python Implementation Program for an Alien Number
import math

# Function to check if a number is prime
def prime(x):
    if x <= 1:  # 0 and 1 are not prime
        return False
    for i in range(2, int(math.sqrt(x) + 1)):  # Loop from 2 to √x
        if x % i == 0:  # If divisible, it's not prime
            return False
    return True  # Otherwise, it's prime

# Function to find the nth prime number
def nprime(n):
    count = 0    # Count of prime numbers found
    i = 2        # Start checking from 2
    val = i      # To store the latest prime found
    while count != n:  # Repeat until we've found the nth prime
        if prime(i):   # If 'i' is prime
            count += 1
            val = i    # Store the current prime
        i += 1         # Check the next number
    return val

# Function to compute the Alien Number
def alien_number(a, b):
    prime_a = nprime(a)  # Get the a-th prime
    prime_b = nprime(b)  # Get the b-th prime
    alien_num = (prime_a + prime_b) - 1  # Apply alien number logic
    print(f"The alien number is {alien_num}")  # Print result

# Accepting two integers from user as input
a, b = map(int, input("Enter any two numbers: ").split())

# Calling the alien number function with inputs
alien_number(a, b)
