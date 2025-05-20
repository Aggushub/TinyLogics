Python Code for - Guess my number game
           where the pc have a number in its mind and we have to guess it

import random

print("🎉 Welcome to my GUESS THE NUMBER game! 🎉")

# Generate a random number in 'imag'
imag = random.randint(1, 100)
user = 0

# Start the guessing loop
while user != imag:
    try:
        user = int(input("Guess a number between 1 and 100: "))
        if user > imag:
            print("🔻 Your guess is higher than my number. Try again!")
        elif user < imag:
            print("🔺 Your guess is lower than my number. Try again!")
    except ValueError:
        print("⚠️ Please enter a valid integer.")

# When guessed correctly
print(f"🎊 Congrats! You guessed the right number: {imag}")



________________________________________________________________________________________
🖥️ Sample Output:

🎉 Welcome to my GUESS THE NUMBER game! 🎉
Guess a number between 1 and 100: 50
🔺 Your guess is lower than my number. Try again!
Guess a number between 1 and 100: 75
🔻 Your guess is higher than my number. Try again!
Guess a number between 1 and 100: 68
🔻 Your guess is higher than my number. Try again!
Guess a number between 1 and 100: 60
🔺 Your guess is lower than my number. Try again!
Guess a number between 1 and 100: 64
🎊 Congrats! You guessed the right number: 64
